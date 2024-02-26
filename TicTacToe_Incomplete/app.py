from flask import Flask, render_template
from tictactoe_solver import check_rows, check_columns, check_diagonals

# TODO: #4: Inside the move function or after a move is made
# TODO: Use the check_rows, check_columns, and check_diagonals functions to determine if there's a winner


app = Flask(__name__)

# TODO: #1
# TODO: Create a list named 'board' with 9 spaces to represent the Tic Tac Toe board
# TODO: Initialize a variable 'current_player' to "X"

@app.route("/")
def index():
    # TODO: Render the 'index.html' template, passing the board and current_player as context
    pass

# TODO: #2
@app.route("/move/<int:position>")
def move(position):
    global board, current_player
    # TODO: Check if the position is valid and the board at the position is empty
    # TODO: Update the board and toggle the current_player
    # TODO: Redirect back to the index page

# The rest of the Flask app setup


if __name__ == '__main__':
    app.run(debug=True)
