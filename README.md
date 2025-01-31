GENERAL CATALOG API
This API provides a comprehensive catalog management system, including authentication, brands, categories, markets, and products. It supports CRUD operations for each entity and uses token-based authentication for secure access.

**Base URL**
  http://127.0.0.1:8000/api/v1/

**Endpoints**
  Authentication
    POST /token/
    Get an access token by providing username and password.

**Brands**
  GET /brands/
    Retrieve a list of all brands.

  GET /brands/{id}/
    Retrieve details of a specific brand.

  POST /brands/
    Create a new brand.

  PUT /brands/{id}/
    Update an existing brand.

  DELETE /brands/{id}/
    Delete a brand.

**Categories**
  GET /categories/
    Retrieve a list of all categories.

  GET /categories/{id}/
    Retrieve details of a specific category.

  POST /categories/
    Create a new category.

  PUT /categories/{id}/
    Update an existing category.

  DELETE /categories/{id}/
    Delete a category.

**Markets**
  GET /markets/
    Retrieve a list of all markets.

  GET /markets/{id}/
    Retrieve details of a specific market.

  POST /markets/
    Create a new market.

  PUT /markets/{id}/
    Update an existing market.

  DELETE /markets/{id}/
    Delete a market.

**Market Products**
  GET /markets/{market_id}/products/
    Retrieve products associated with a specific market.

  POST /markets/{market_id}/products/
    Add a product to a market.

  GET /markets/{market_id}/products/{product_id}/
    Retrieve details of a specific product in a market.

  PUT /markets/{market_id}/products/{product_id}/
    Update a product in a market.

  DELETE /markets/{market_id}/products/{product_id}/
    Remove a product from a market.

**Market Product Prices**
  POST /markets/{market_id}/products/{product_id}/prices/
    Add a price for a product in a market.

  GET /markets/{market_id}/products/{product_id}/prices/
    Retrieve price history for a product in a market.

**Products**
  GET /products/
    Retrieve a list of all products.

  GET /products/{id}/
    Retrieve details of a specific product.

  POST /products/
    Create a new product.

  PUT /products/{id}/
    Update an existing product.

  DELETE /products/{id}/
    Delete a product.

**Authentication**
  The API uses Bearer Token authentication. Include the token in the Authorization header for protected endpoints:
  Authorization: Bearer <token>

Example Requests

**Get Token**
  curl -X POST http://127.0.0.1:8000/api/v1/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "joão", "password": "joao1234"}'

**Create a Brand**
  curl -X POST http://127.0.0.1:8000/api/v1/brands/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name": "Bauducco", "description": "Exemplo de descrição"}'

**Get Products in a Market**
  curl -X GET http://127.0.0.1:8000/api/v1/markets/4/products/ \
  -H "Authorization: Bearer <token>"


This API is designed for managing a catalog system with flexibility and security. For more details, refer to the Postman collection or the API documentation.
