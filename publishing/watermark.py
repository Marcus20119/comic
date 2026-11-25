"""Export watermarked copies of comic art without editing the originals."""

import argparse
from pathlib import Path
from tempfile import NamedTemporaryFile

from PIL import Image, ImageDraw, ImageFont, ImageOps

FORMATS = {".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG", ".webp": "WEBP"}


def watermark(image, handle, opacity, font_path, lift):
    image = image.convert("RGBA")
    width, height = image.size
    short = min(image.size)
    margin = max(1, round(short * 0.016))
    size = max(1, round(short * 0.026))
    while size > 0:
        font = (ImageFont.truetype(font_path, size) if font_path
                else ImageFont.load_default(size=size))
        left, top, right, bottom = font.getbbox(handle)
        px, py = max(1, round(size * 0.42)), max(1, round(size * 0.26))
        w, h = right - left + 2 * px, bottom - top + 2 * py
        if w + 2 * margin <= width and h + 2 * margin <= height:
            break
        size -= 1
    else:
        raise ValueError("image is too small for the watermark")

    badge = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(badge)
    draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=max(1, round(size * 0.28)),
                           fill=(15, 15, 18, round(255 * opacity / 100)))
    draw.text((px - left, py - top), handle, font=font, fill="white")
    image.alpha_composite(badge, (width - margin - w, max(0, height - margin - h - round(short * lift / 100))))
    return image


def export(source, target, args):
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.parent.resolve().is_relative_to(args.output):
        raise ValueError("output subfolder resolves outside watermark/")
    with Image.open(source) as original:
        if getattr(original, "is_animated", False):
            raise ValueError("animated images are not supported")
        image = watermark(ImageOps.exif_transpose(original), args.handle, args.opacity, args.font, args.lifts.get(source.name, 0))
        fmt = FORMATS[source.suffix.lower()]
        options = {"icc_profile": original.info["icc_profile"]} if original.info.get("icc_profile") else {}
        if fmt == "JPEG":
            image = image.convert("RGB")
            options.update(quality=95, subsampling=0)
        elif fmt == "WEBP":
            options.update(lossless=True)
        # Replace the derivative only after encoding succeeds.
        with NamedTemporaryFile(dir=target.parent, prefix=".watermark-", delete=False) as temp:
            temporary = Path(temp.name)
        try:
            image.save(temporary, format=fmt, **options)
            temporary.replace(target)
        finally:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="An art folder, chapter, series, or workspace root")
    parser.add_argument("--handle", default="@buckuroo20119")
    parser.add_argument("--opacity", type=int, default=68, metavar="PERCENT", help="Badge opacity (default: 68)")
    parser.add_argument("--font", help="Optional TrueType/OpenType font path")
    parser.add_argument("--lift", action="append", default=[], metavar="FILENAME=PERCENT",
                        help="Move the badge up by a percent of the short edge for a matching filename")
    args = parser.parse_args()
    args.lifts = {}
    for rule in args.lift:
        try:
            name, amount = rule.rsplit("=", 1)
            lift = int(amount)
            if not name or not 0 <= lift <= 25:
                raise ValueError
        except ValueError:
            parser.error("--lift requires FILENAME=PERCENT, with a percent from 0 to 25")
        args.lifts[name] = lift
    if not args.handle.strip() or not args.handle.isprintable():
        parser.error("--handle must be nonempty printable text")
    if not 0 <= args.opacity <= 100:
        parser.error("--opacity must be between 0 and 100")
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    if "watermark" in root.parts:
        parser.error("select art/ or a parent outside watermark/")

    art_dirs = [root] if root.name == "art" else sorted(
        path for path in root.rglob("art") if path.is_dir() and not path.is_symlink()
        and not {"art", "watermark", ".git"}.intersection(path.relative_to(root).parts[:-1])
    )
    count = failed = 0
    for art in art_dirs:
        args.output = art.with_name("watermark")
        if args.output.resolve() != args.output:
            parser.error(f"output must not redirect to another directory: {args.output}")
        for source in sorted(art.rglob("*")):
            if source.is_symlink() or not source.is_file() or source.suffix.lower() not in FORMATS:
                continue
            target = args.output / source.relative_to(art)
            try:
                export(source, target, args)
            except (OSError, ValueError) as error:
                print(f"ERROR {source}: {error}")
                failed += 1
            else:
                print(target)
                count += 1
    print(f"Exported {count} image(s); {failed} failed.")
    return 1 if failed or not count else 0


if __name__ == "__main__":
    raise SystemExit(main())
