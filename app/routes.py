from flask import Blueprint, current_app, jsonify, request

bp = Blueprint("main", __name__)

# Simple in-memory store (resets on restart). Swap for a real DB as needed.
ITEMS: dict[int, dict] = {}
_next_id = 1


@bp.get("/")
def index():
    return jsonify(message=f"Welcome to {current_app.config['APP_NAME']}")


@bp.get("/health")
def health():
    return jsonify(status="ok")


@bp.get("/api/items")
def list_items():
    return jsonify(list(ITEMS.values()))


@bp.post("/api/items")
def create_item():
    global _next_id
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify(error="'name' is required"), 400
    item = {"id": _next_id, "name": name}
    ITEMS[_next_id] = item
    _next_id += 1
    return jsonify(item), 201


@bp.get("/api/items/<int:item_id>")
def get_item(item_id: int):
    item = ITEMS.get(item_id)
    if item is None:
        return jsonify(error="not found"), 404
    return jsonify(item)


@bp.delete("/api/items/<int:item_id>")
def delete_item(item_id: int):
    if ITEMS.pop(item_id, None) is None:
        return jsonify(error="not found"), 404
    return "", 204
