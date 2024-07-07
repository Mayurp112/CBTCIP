from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(store_info, transaction_id, customer_name, items, tax_rate, discount=0, payment_method="Credit Card"):
    # Set the name of the receipt PDF
    receipt_name = f"receipt_{transaction_id}.pdf"

    # Create a canvas object with letter page size
    c = canvas.Canvas(receipt_name, pagesize=letter)

    # Store information
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 780, store_info["name"])

    c.setFont("Helvetica", 12)
    c.drawString(100, 760, store_info["address"])
    c.drawString(100, 745, f"Contact: {store_info['contact']}")

    # Title and transaction details
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 720, "Payment Receipt")

    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Transaction ID: {transaction_id}")
    c.drawString(100, 685, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 670, f"Customer Name: {customer_name}")
    c.drawString(100, 655, f"Payment Method: {payment_method}")

    # Add items header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 630, "Items")
    c.drawString(300, 630, "Price")

    # Add items
    c.setFont("Helvetica", 12)
    y_position = 610
    for item, price in items.items():
        c.drawString(100, y_position, item)
        c.drawString(300, y_position, f"${price:.2f}")
        y_position -= 20

    # Calculate subtotal, tax, discount, and total amount
    subtotal = sum(items.values())
    tax = subtotal * tax_rate
    total_amount = subtotal + tax - discount

    # Add subtotal, tax, discount, and total amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_position - 20, "Subtotal")
    c.drawString(300, y_position - 20, f"${subtotal:.2f}")
    c.drawString(100, y_position - 40, f"Tax ({tax_rate * 100:.0f}%)")
    c.drawString(300, y_position - 40, f"${tax:.2f}")
    c.drawString(100, y_position - 60, "Discount")
    c.drawString(300, y_position - 60, f"${discount:.2f}")
    c.drawString(100, y_position - 80, "Total Amount")
    c.drawString(300, y_position - 80, f"${total_amount:.2f}")

    # Add a thank you note
    c.setFont("Helvetica", 12)
    c.drawString(100, y_position - 120, "Thank you for shopping with us!")

    # Save the PDF
    c.save()

store_info = {
    "name": "ABC Store",
    "address": "123 Main Street, City, State, ZIP",
    "contact": "123-456-7890"
}
transaction_id = "TXN123456"
customer_name = "John Doe"
items = {
    "Product 1": 25.00,
    "Product 2": 40.00,
    "Product 3": 15.50,
}
tax_rate = 0.07  # 7% tax
discount = 5.00  # $5 discount
payment_method = "Credit Card"

create_receipt(store_info, transaction_id, customer_name, items, tax_rate, discount, payment_method)
