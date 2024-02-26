from flask import Flask, render_template, request, redirect, url_for
from tictactoe_solver import check_rows, check_columns, check_diagonals

app = Flask(__name__)

# Initialize an empty board
board = [" " for _ in range(9)]
current_player = "X"
winner = None

@app.route("/")
def index():
    return render_template("index.html", board=board, current_player=current_player)

@app.route("/move/<int:position>")
def move(position):
    global winner
    global current_player
    
    if board[position] == " ":
        board[position] = current_player
        current_player = "O" if current_player == "X" else "X"
        
        if check_rows(board) != "False":
            winner = check_rows(board)
        if check_columns(board) != "False":
            winner = check_columns(board)
        if check_diagonals(board) != "False":
            winner = check_diagonals(board)
        
        print(winner)
        
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)


