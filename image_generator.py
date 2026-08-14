from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import io

BACKGROUND_COLORS = [
    '#6C5CE7',  # Фиолетовый
    '#00B894',  # Мятный/зеленый
    '#E84393',  # Розовый
    '#0984E3',  # Голубой/синий
    '#2D3436',  # Тёмный
    '#A29BFE'   # Светло-фиолетовый
]

def create_card(text: str) -> io.BytesIO:
    width, height = 1080, 1080
    
    bg_color = random.choice(BACKGROUND_COLORS)
    
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    card_w, card_h = 900, 450
    card_x = (width - card_w) // 2
    card_y = (height - card_h) // 2
    
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_w, card_y + card_h],
        radius=30,
        fill='white'
    )
    
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    except IOError:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(text, width=35)
    
    draw.text(
        (width // 2, height // 2),
        wrapped_text,
        fill='black',
        font=font,
        anchor="mm",
        align="center"
    )
    
    bio = io.BytesIO()
    bio.name = 'question.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    
    return bio
