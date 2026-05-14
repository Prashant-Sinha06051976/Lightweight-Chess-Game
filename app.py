
import streamlit as st
import chess
import plotly.graph_objects as go

from engine_utils import (
    get_engine_move,
    get_top_moves,
    evaluate_position
)

from game_analytics import build_game_analysis

st.set_page_config(
    page_title="Dynamic Chess AI",
    layout="wide"
)

st.title("♟ Dynamic Chess AI")

if "board" not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

mode = st.sidebar.selectbox(
    "Game Mode",
    ["Play vs Computer", "Online Multiplayer"]
)

st.subheader("Board Position")
st.code(str(board))

move_input = st.text_input(
    "Enter move (UCI format)",
    placeholder="e2e4"
)

if st.button("Play Move"):
    try:
        move = chess.Move.from_uci(move_input)

        if move in board.legal_moves:
            board.push(move)
            st.success(f"Move played: {move}")
        else:
            st.error("Illegal move")

    except Exception:
        st.error("Invalid move format")

if mode == "Play vs Computer":

    if st.button("Computer Move"):
        ai_move = get_engine_move(board)

        if ai_move:
            board.push(ai_move)
            st.success(f"AI played: {ai_move}")

st.subheader("Top Suggested Moves")

suggestions = get_top_moves(board)

for idx, move in enumerate(suggestions, start=1):
    st.write(f"{idx}. {move}")

st.subheader("Position Evaluation")

evaluation = evaluate_position(board)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=evaluation,
    title={"text": "Engine Score"}
))

st.plotly_chart(fig, use_container_width=True)

st.subheader("Advanced Analytics")
st.dataframe(build_game_analysis(board))

if board.is_checkmate():
    st.error("Checkmate")

if board.is_stalemate():
    st.warning("Stalemate")
