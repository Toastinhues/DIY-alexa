
import tkinter as tk
import colorsys
import math

LED_COUNT = 30
running = True
mode = "rainbow"
frame = 0
solid_color = "#0080ff"

BG = "#20242b"
WHITE = "#ffffff"

root = tk.Tk()
root.title("DIY Alexa - Underglow Simulator")
root.geometry("520x390")
root.configure(bg=BG)

title = tk.Label(
    root,
    text="DIY Alexa RGB Underglow",
    font=("Arial", 17, "bold"),
    bg=BG,
    fg=WHITE,
)
title.pack(pady=12)

canvas = tk.Canvas(
    root,
    width=460,
    height=115,
    bg="#101216",
    highlightthickness=0,
)
canvas.pack(pady=8)

status = tk.Label(
    root,
    text="Mode: Rainbow",
    bg=BG,
    fg=WHITE,
    font=("Arial", 11),
)
status.pack(pady=6)


def set_mode(new_mode):
    global mode, frame
    mode = new_mode
    frame = 0
    status.config(text=f"Mode: {new_mode.title()}")


def choose_color():
    global solid_color
    from tkinter.colorchooser import askcolor

    result = askcolor(
        color=solid_color,
        title="Choose an underglow colour",
    )
    if result[1]:
        solid_color = result[1]
        restart_animation("solid")


def draw_leds():
    global frame

    canvas.delete("all")
    width = 460
    spacing = width / LED_COUNT

    for i in range(LED_COUNT):
        if mode == "off":
            color = "#181818"

        elif mode == "solid":
            color = solid_color

        elif mode == "breathe":
            brightness = (math.sin(frame / 15) + 1) / 2
            rgb = tuple(
                int(int(solid_color[j:j + 2], 16) * brightness)
                for j in (1, 3, 5)
            )
            color = "#%02x%02x%02x" % rgb

        else:
            hue = ((i / LED_COUNT) + frame / 100) % 1
            rgb = colorsys.hsv_to_rgb(hue, 1, 1)
            color = "#%02x%02x%02x" % tuple(
                int(channel * 255) for channel in rgb
            )

        x = i * spacing + 3
        canvas.create_oval(
            x, 25, x + spacing - 6, 25 + spacing - 6,
            fill=color,
            outline="",
        )

    frame += 1

    if mode in ("rainbow", "breathe"):
        root.after(40, draw_leds)


def restart_animation(new_mode):
    set_mode(new_mode)
    draw_leds()


controls = tk.Frame(root, bg=BG)
controls.pack(pady=10)

for text, value in [
    ("Rainbow", "rainbow"),
    ("Breathe", "breathe"),
    ("Choose Colour", "choose"),
    ("Off", "off"),
]:
    action = choose_color if value == "choose" else (
        lambda v=value: restart_animation(v)
    )

    tk.Button(
        controls,
        text=text,
        command=action,
        padx=9,
    ).pack(side="left", padx=4)

draw_leds()
root.mainloop()
