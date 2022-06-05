import tkinter as tk

import settings
import utils
from cell import Cell


def main():
    root = tk.Tk()

    # Override the settings of the window
    root.title('Minesweeper Game')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.resizable(False, False)
    root.configure(bg='black')

    # Create frames
    top_frame = tk.Frame(
        root,
        width=settings.WIDTH,
        height=utils.height_prct(25),
        bg='red',
    )
    top_frame.place(x=0, y=0)

    left_frame = tk.Frame(
        root,
        width=utils.width_prct(25),
        height=utils.height_prct(75),
        bg='blue',
    )
    left_frame.place(x=0, y=utils.height_prct(25))

    center_frame = tk.Frame(
        root,
        width=utils.width_prct(75),
        height=utils.height_prct(75),
        bg='green',
    )
    center_frame.place(
        x=utils.width_prct(25),
        y=utils.height_prct(25)
   )

    # Add the tile of mines to the center_frame
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid(
                column=x, row=y
            )

    # Call the label from the Cell class
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(x=0, y=0)

    Cell.randomize_mines()

    # Run the main loop
    root.mainloop()


if __name__ == '__main__':
    main()