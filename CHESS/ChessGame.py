WIDTH, HEIGHT = 1000,1000
TILE_SIZE = WIDTH // 8

class Piece:
    def __init__(self, name, color, row, col):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        folder = "WhitePieces" if color == "white" else "BlackPieces"
        self.img = load_image(f"{folder}/{color}{name}.png")

    def display(self):
        x = self.col * TILE_SIZE
        y = self.row * TILE_SIZE
        tint(255, 255, 255, 220) 
        image(self.img, x, y, TILE_SIZE, TILE_SIZE)

board = [None] * 64
selected_index = None
turn = "white"

def setup():
    size(WIDTH, HEIGHT)
    smooth()
    reset_game()

def reset_game():
    global board, selected_index, turn
    board = [None] * 64
    selected_index = None
    turn = "white"

    layout = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
    
    for i, name in enumerate(layout):
        board[i] = Piece(name, "black", 0, i)
        board[i + 8] = Piece("pawn", "black", 1, i)
        board[i + 48] = Piece("pawn", "white", 6, i)
        board[i + 56] = Piece(name, "white", 7, i)

def draw():
    draw_grid()
    for piece in board:
        if piece:
            piece.display()
    
    if selected_index is not None:
        no_fill()
        stroke(0, 255, 0)
        stroke_weight(4)
        rect((selected_index % 8) * TILE_SIZE, (selected_index // 8) * TILE_SIZE, TILE_SIZE, TILE_SIZE)

def draw_grid():
    for row in range(8):
        for col in range(8):
            fill(235, 235, 208) if (row + col) % 2 == 0 else fill(119, 148, 85)
            no_stroke()
            rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)

def is_path_clear(r1, c1, r2, c2):
    dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
    dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
    curr_r, curr_c = r1 + dr, c1 + dc
    while (curr_r, curr_c) != (r2, c2):
        if board[curr_r * 8 + curr_c] is not None:
            return False
        curr_r += dr
        curr_c += dc
    return True

def is_valid_move(p, start_r, start_c, end_r, end_c):
    target = board[end_r * 8 + end_c]
    if target and target.color == p.color:
        return False
    
    dr = abs(end_r - start_r)
    dc = abs(end_c - start_c)

    if p.name == "pawn":
        direction = -1 if p.color == "white" else 1
        if start_c == end_c and target is None:
            if end_r - start_r == direction:
                return True
            if (p.row == 6 or p.row == 1) and end_r - start_r == 2 * direction:
                return board[(start_r + direction) * 8 + start_c] is None
        if dr == 1 and dc == 1 and target and target.color != p.color:
            return end_r - start_r == direction

    elif p.name == "rook":
        if start_r == end_r or start_c == end_c:
            return is_path_clear(start_r, start_c, end_r, end_c)

    elif p.name == "knight":
        return (dr == 2 and dc == 1) or (dr == 1 and dc == 2)

    elif p.name == "bishop":
        if dr == dc:
            return is_path_clear(start_r, start_c, end_r, end_c)

    elif p.name == "queen":
        if dr == dc or start_r == end_r or start_c == end_c:
            return is_path_clear(start_r, start_c, end_r, end_c)

    elif p.name == "king":
        return dr <= 1 and dc <= 1

    return False

def is_in_check(color):
    king = next((p for p in board if p and p.name == "king" and p.color == color), None)
    if not king:
        return False
    for p in board:
        if p and p.color != color:
            if is_valid_move(p, p.row, p.col, king.row, king.col):
                return True
    return False

def has_any_valid_move(color):
    for i, p in enumerate(board):
        if p and p.color == color:
            for r in range(8):
                for c in range(8):
                    target = board[r*8+c]
                    if is_valid_move(p, p.row, p.col, r, c):
                        board[i] = None
                        board[r*8+c] = p
                        old_row, old_col = p.row, p.col
                        p.row, p.col = r, c
                        if not is_in_check(color):
                            board[i] = p
                            board[r*8+c] = target
                            p.row, p.col = old_row, old_col
                            return True
                        board[i] = p
                        board[r*8+c] = target
                        p.row, p.col = old_row, old_col
    return False

def check_game_status():
    if is_in_check(turn):
        if not has_any_valid_move(turn):
            print(f"Checkmate! { 'White' if turn == 'black' else 'Black' } wins!")
        else:
            print(f"{turn.capitalize()} is in check!")
    else:
        if not has_any_valid_move(turn):
            print("Stalemate!")

def mouse_pressed():
    global selected_index, turn
    col, row = mouse_x // TILE_SIZE, mouse_y // TILE_SIZE
    index = row * 8 + col
    
    if selected_index is None:
        if board[index] and board[index].color == turn:
            selected_index = index
    else:
        p = board[selected_index]
        if is_valid_move(p, p.row, p.col, row, col):
            p.row, p.col = row, col
            board[index] = p
            board[selected_index] = None
            turn = "black" if turn == "white" else "white"
            selected_index = None
            check_game_status()
        elif board[index] and board[index].color == turn:
            selected_index = index 
        else:
            selected_index = None 
