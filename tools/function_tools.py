from agents import function_tool
from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    product_name: str
    features: List[str]
    description: str
    price: float
    currency: str
    original_price: float = None
    discount: str = None

# Product Data (Store this outside the function as a constant or mock DB)
PRODUCTS = [
    Product(
        id=1,
        product_name="Smartphone X1",
        features=["6.5-inch AMOLED display", "128GB storage", "48MP camera", "5G connectivity"],
        description="A high-performance smartphone with a vibrant AMOLED display and advanced camera system for stunning photos.",
        price=699.99,
        currency="USD"
    ),
    Product(
        id=51,
        product_name="Syltherine",
        features=["Solid Teak Wood", "Velvet Upholstery"],
        description="Stylish cafe chair made with high-quality solid teak wood and comfortable velvet upholstery.",
        price=2500000,
        original_price=3500000,
        currency="IDR"
    ),
    Product(
        id=52,
        product_name="Lolito",
        features=["Premium Leather", "Ergonomic Design", "Modular Sections"],
        description="Luxury big sofa designed for ultimate comfort and style, featuring premium leather and a modular design.",
        price=7000000,
        original_price=14000000,
        discount="50%",
        currency="IDR"
    )
]

# Product Info Tool Function
@function_tool
async def product_info(product_name: str) -> str:
    """
    Provide information about a product by its name.
    """
    for product in PRODUCTS:
        if product_name.lower() in product.product_name.lower():
            return f"Product Name: {product.product_name}\nFeatures: {', '.join(product.features)}\nDescription: {product.description}\nPrice: {product.price} {product.currency}\nDiscount: {product.discount or 'N/A'}"

    return "Product not found. Please try another name."
