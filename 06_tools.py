from langchain_core.tools import tool

@tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a percentage discount."""
    return round(price - (price * discount_percent / 100), 2)

@tool
def get_course_level(topic: str) -> str:
    """Return a simple recommended level for a programming topic."""
    beginner_topics = {"python", "git", "langchain basics"}
    if topic.lower() in beginner_topics:
        return "Beginner"
    return "Intermediate"

print(calculate_discount.invoke({
    "price": 1000,
    "discount_percent": 15,
}))

print(get_course_level.invoke({
    "topic": "Python",
}))
