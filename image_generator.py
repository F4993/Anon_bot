from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import io
import groups

BACKGROUND_COLORS = [
    '#6C5CE7',
    '#00B894',
    '#E84393',
    '#0984E3',
    '#2D3436',
    '#A29BFE'
]

def create_card(text: str) -> io.BytesIO:
    width, height = 1080, 1080
    bg_color = random.choice(BACKGROUND_COLORS)
    
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font_main = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
        font_pattern = ImageFont.truetype("DejaVuSans-Bold.ttf", 45)
        font_tag = ImageFont.truetype("DejaVuSans-Bold.ttf", 26)
        font_icon = ImageFont.truetype("DejaVuSans-Bold.ttf", 55)
    except IOError:
        font_main = font_pattern = font_tag = font_icon = ImageFont.load_default()

    pattern_color = (255, 255, 255, 40)
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)

    step = 130
    for y in range(-50, height + 100, step):
        for x in range(-50, width + 100, step):
            shift = 40 if (y // step) % 2 == 0 else 0
            draw_overlay.text((x + shift, y), "?", fill=pattern_color, font=font_pattern)

    img.paste(Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB'))
    draw = ImageDraw.Draw(img)

    card_w, card_h = 900, 480
    card_x = (width - card_w) // 2
    card_y = (height - card_h) // 2

    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_w, card_y + card_h],
        radius=35,
        fill='white'
    )

    circle_r = 60
    circle_center = (width // 2, card_y)
    draw.ellipse(
        [circle_center[0] - circle_r, circle_center[1] - circle_r,
         circle_center[0] + circle_r, circle_center[1] + circle_r],
        fill='#00A8FF',
        outline='white',
        width=6
    )
    draw.text((circle_center[0], circle_center[1] - 5), "🎭", fill='white', font=font_icon, anchor="mm")

    # 4. Текст анонимки по центру
    wrapped_text = textwrap.fill(text, width=32)
    draw.text(
        (width // 2, height // 2),
        wrapped_text,
        fill='#111111',
        font=font_main,
        anchor="mm",
        align="center"
    )

    bot_tag = getattr(groups, 'BOT_USERNAME', '@anon_bot')
    
    tag_w, tag_h = 240, 50
    tag_x = (width - tag_w) // 2
    tag_y = card_y + card_h - (tag_h // 2)

    draw.rounded_rectangle(
        [tag_x, tag_y, tag_x + tag_w, tag_y + tag_h],
        radius=25,
        fill='#00A8FF'
    )
    draw.text(
        (width // 2, tag_y + (tag_h // 2)),
        bot_tag,
        fill='white',
        font=font_tag,
        anchor="mm"
    )

    bio = io.BytesIO()
    bio.name = 'question.png'
    img.save(bio, 'PNG')
    bio.seek(0)

    return bio
