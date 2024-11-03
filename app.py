import matplotlib.pyplot as plt
import numpy as np

# Define the board and piece symbols using Unicode
board_size = 8

# Piece symbols
pieces = {
    "black": {
        "king": "\u265A", "queen": "\u265B", "rook": "\u265C",
        "bishop": "\u265D", "knight": "\u265E", "pawn": "\u265F"
    },
    "white": {
        "king": "\u2654", "queen": "\u2655", "rook": "\u2656",
        "bishop": "\u2657", "knight": "\u2658", "pawn": "\u2659"
    }
}

# Starting position
chessboard = [
    [pieces["black"]["rook"], pieces["black"]["knight"], pieces["black"]["bishop"], pieces["black"]["queen"],
     pieces["black"]["king"], pieces["black"]["bishop"], pieces["black"]["knight"], pieces["black"]["rook"]],
    [pieces["black"]["pawn"]] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [pieces["white"]["pawn"]] * 8,
    [pieces["white"]["rook"], pieces["white"]["knight"], pieces["white"]["bishop"], pieces["white"]["queen"],
     pieces["white"]["king"], pieces["white"]["bishop"], pieces["white"]["knight"], pieces["white"]["rook"]],
]

# Create the checkerboard pattern
board_colors = np.zeros((board_size, board_size))
board_colors[1::2, ::2] = 1  # Black squares on odd rows
board_colors[::2, 1::2] = 1  # Black squares on even rows

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Use a black and white color map
ax.imshow(board_colors, cmap="gray", vmin=0, vmax=1)

# Place the pieces on the board
for i in range(board_size):
    for j in range(board_size):
        piece = chessboard[i][j]
        if piece:
            ax.text(j, i, piece, ha="center", va="center", fontsize=28, color="black" if board_colors[i, j] == 1 else "white")

# Set the grid and labels for rows and columns
ax.set_xticks(np.arange(board_size) - 0.5, minor=True)
ax.set_yticks(np.arange(board_size) - 0.5, minor=True)
ax.grid(which="minor", color="black", linestyle="-", linewidth=2)

# Labels for rows and columns
columns = ["1", "2", "3", "4", "5", "6", "7", "8"]
rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

# Set labels for x and y axes
ax.set_xticks(range(board_size))
ax.set_xticklabels(columns, fontweight='bold', fontsize=12)
ax.set_yticks(range(board_size))
ax.set_yticklabels(rows, fontweight='bold', fontsize=12)

# Remove axis labels and ticks
ax.tick_params(bottom=False, left=False)

# Add a brown border around the board
plt.gca().add_patch(plt.Rectangle((0 - 0.5, 0 - 0.5), 8, 8,
                                  linewidth=20, edgecolor='#3a2c23', facecolor='none'))

plt.show()
