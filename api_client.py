from flask import Flask, jsonify, request, abort
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Tüm isteklere CORS desteği eklemek için

# Stok verisi (örnek amaçlı)
stock = [
    {"id": 1, "name": "Ürün 1", "quantity": 100},
    {"id": 2, "name": "Ürün 2", "quantity": 200}
]

# OpenAPI JSON verisi
openapi_json = {
    "openapi": "3.0.0",
    "info": {
        "title": "Stok API - OpenAPI 3.0",
        "description": "Bu, OpenAPI 3.0 belirtmesine dayalı bir örnek Stok API'sidir. Bu API, stokları yönetmek için uç noktalar sağlar. Bu API'yi kullanarak stok ekleyebilir, güncelleyebilir, silebilir ve alabilirsiniz.",
        "version": "1.0.0"
    },
    "servers": [
        {
            "url": "http://localhost:5000"
        }
    ],
    "tags": [
        {
            "name": "stock",
            "description": "Stoklar hakkındaki işlemler"
        }
    ],
    "paths": {
        "/api/v1/stock": {
            "get": {
                "tags": ["stock"],
                "summary": "Tüm stokları al",
                "responses": {
                    "200": {
                        "description": "başarılı işlem",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/StockItem"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["stock"],
                "summary": "Yeni bir stok ekleyin",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/StockItem"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "başarılı işlem",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/StockItem"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": ["stock"],
                "summary": "Tüm stokları sil",
                "responses": {
                    "204": {"description": "başarılı işlem"}
                }
            },
            "put": {
                "tags": ["stock"],
                "summary": "Tüm stokları güncelle",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/StockItem"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "başarılı işlem",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/StockItem"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "StockItem": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "format": "int64"},
                    "name": {"type": "string"},
                    "quantity": {"type": "integer"}
                }
            }
        }
    }
}

# OpenAPI JSON'u sunmak için rotayı belirtme
@app.route('/openapi.json')
def serve_openapi():
    return jsonify(openapi_json)

# Stok isteklerini işlemek için rotayı belirtme
@app.route('/api/v1/stock', methods=['GET'])
def get_stock():
    return jsonify(stock)

@app.route('/api/v1/stock', methods=['POST'])
def add_stock():
    if not request.json or 'name' not in request.json or 'quantity' not in request.json:
        abort(400)
    item = {
        'id': stock[-1]['id'] + 1,
        'name': request.json['name'],
        'quantity': request.json['quantity']
    }
    stock.append(item)
    return jsonify(item), 201

@app.route('/api/v1/stock', methods=['DELETE'])
def delete_stock():
    del stock[:]
    return '', 204

@app.route('/api/v1/stock', methods=['PUT'])
def update_stock():
    if not request.json:
        abort(400)
    stock.clear()
    for item in request.json:
        if 'name' not in item or 'quantity' not in item:
            abort(400)
        stock.append({
            'id': item.get('id'),
            'name': item.get('name'),
            'quantity': item.get('quantity')
        })
    return jsonify(stock), 200

# Swagger UI Blueprint oluşturma
swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    '/openapi.json',
    config={'app_name': "Stok API Belgeleri"}
)

# Swagger UI Blueprint'ini kaydetme
app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')

if __name__ == '__main__':
    app.run(debug=True)

