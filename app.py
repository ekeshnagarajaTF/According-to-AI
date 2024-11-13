from flask import Flask
from fpdf import FPDF
import json
from orderfunction import generate_order_id

app = Flask(__name__)

count_file = "report_count.json"
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Analysis Report", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_title(self, title):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, title, align="C", ln=True)
        self.ln(10)

    def add_paragraph(self, text, bold= False, underline = False, same_line = False):
        style = "" 
        if bold: 
            style += "B"

        if underline:
            style += "U"  
        self.set_font("Arial", style, 12)
        self.multi_cell(0, 10, text)
        self.ln(10)

    def add_table(self, data):
        self.set_font("Arial", "B", 12)
        col_widths = [30, 100, 30]
        headers = ["Item", "Description", "Price"]

        # Header row
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C")
        self.ln()

        # Table rows
        self.set_font("Arial", "", 12)
        for row in data:
            for i, item in enumerate(row):
                self.cell(col_widths[i], 10, item, border=1, align="C")
            self.ln()

def create_pdf_report():
    pdf = PDFReport()
    pdf.add_page()

    # Title
    pdf.add_title("Client Sentiment Analysis")

    # Body text
    json_body = '''{
    "Call Structure": "The call was structured with the client initiating the conversation by introducing the SmartHome Light System, followed by the employee asking for the order number. The client then provided more details about the product, including its features, pricing, and trial period. The employee expressed interest in the product and asked more questions, leading to a discussion about the setup process and the trial period. The client then expressed interest in trying out the product and the employee offered to send details for ordering online. The call ended with the employee offering to email the information and encouraging the client to reach out with any questions.",
    "Pitch or Sell": "Yes, there was a pitch or sell during the conversation. The client mentioned the benefits of the SmartHome Light System, such as being able to control lights from a phone, saving energy, compatibility with other devices, affordability, different packages, and a 30-day trial period with a full refund option. The client also highlighted the ease of setup and the availability of a customer support team. The employee also acknowledged the benefits of remote control and the trial period. Additionally, the employee offered to send the client details to get started with the purchase.",
    "Call Purpose": "The call's purpose was for the client to inform the employee about the SmartHome Light System, discuss its features and benefits, including remote control and energy saving capabilities, mention the affordability and trial period, and express interest in trying out the product. The employee provided information on how to order the product and offered to send the details via email. Overall, the call was focused on introducing and potentially selling the SmartHome Light System to the client.",
    "Customer Feedback": "The customer told the employee about their SmartHome Light System, highlighting its features such as controlling lights from a phone, saving energy, compatibility with other devices, affordability, different packages, and a 30-day trial period for testing. The customer also mentioned the ease of setup, the customer support team, and their interest in controlling lights from their phone due to forgetting to turn them off. Finally, the customer expressed interest in getting started with the SmartHome Light System and requested details to order online.",
    "Our Response": "We responded to the customer by providing information about the SmartHome Light System, answering their questions, explaining the pricing and trial period, offering to send them details on how to get started, and assuring them that they can reach out if they have any further questions.",
    "Pitched and Received": "The client pitched the SmartHome Light System to the employee during the conversation. The client described the system as a way to control lights from a phone, save energy, and mentioned its compatibility with other devices. The client also highlighted the affordability of the system and the 30-day trial period for testing it out. \\n\\nThe employee seemed interested in the idea of smart lights and found the concept of controlling them remotely helpful, especially when forgetting to turn them off. The employee also expressed interest in the trial period and seemed open to trying out the SmartHome Light System. Ultimately, the pitch of the SmartHome Light System was received positively by the employee.",
    "Customer Sentiment": "The general customer sentiment in this conversation appears to be positive. The client expresses enthusiasm and excitement about the SmartHome Light System, highlighting its features, affordability, and the trial period. The client also seems interested in the product and appreciates the assistance provided by the employee. Overall, the client's tone is upbeat and positive throughout the conversation.",
    "Negative Sentiment": "Based on the conversation provided, there doesn't seem to be any negative customer sentiment expressed by the client. The client seems enthusiastic about the SmartHome Light System, highlighting its benefits, affordability, and the trial period. The client also appreciates the ease of setup and customer support. Therefore, there doesn't appear to be any negative sentiment that could have caused dissatisfaction.",
    "Action Items": "Action items:\\n 1. The client expressed interest in the SmartHome Light System and may potentially make a purchase.\\n2. The employee will email the client the details and a link to the website for ordering.\\n3. The client will review the information sent by the employee and potentially place an order.\\n\\nNext steps:\\n1. The client will receive the email with details and the website link.\\n2. The client will review the information and make a decision on whether to purchase the SmartHome Light System.\\n3. If the client decides to proceed, they will place an order online.\\n\\nResults:\\n1. The client may potentially purchase the SmartHome Light System.\\n2. The employee successfully provided information and assistance to the client.\\n3. The client expressed interest in the product and showed willingness to explore further by reviewing the details sent via email.",
    "Missed Opportunities": "Based on the conversation provided, it seems like the employee could have been more proactive in promoting the benefits of the SmartHome Light System and potentially upselling the client to a higher package. The employee could have also provided more detailed information about the different packages available and highlighted any special features or discounts that may apply.\\n\\nAdditionally, the employee could have moved faster by immediately providing the client with the link to order online or offering to assist in placing the order during the call. This would have made the process more convenient for the client and potentially closed the sale faster.\\n\\nIn terms of customer service, the employee could have reassured the client about the return policy and provided more information about the customer support team to instill confidence in the product and company. Overall, there were missed opportunities to sell, move faster, and provide better service to the customer during this conversation.",
    "Language Barrier": "Based on the conversation provided, there doesn't seem to be any clear indication of a language barrier. Both the client and employee were able to communicate their points effectively, albeit with some hesitations and pauses in speech. The client used casual language such as \\"like\\" and \\"um\\" but it didn't hinder the understanding of the conversation. The employee also responded appropriately and provided information as needed. Therefore, it appears that there was no significant language barrier in this customer service call conversation.",
    "CRM/Deal Updates": "Some CRM/deal relevant updates from the conversation include:\\n1. The client expressing interest in the SmartHome Light System and discussing its features and pricing.\\n2. The employee providing information about the trial period and the process of returning the product if not satisfied.\\n3. The client showing interest in trying out the product and asking how to get started.\\n4. The employee offering to send the client details to order the product online.\\n5. The client agreeing to receive the details and expressing interest in taking a look.\\n6. The employee confirming that they will email the information and encouraging the client to reach out with any questions.",
    "Customer Interest": "Based on the conversation, the client seems quite interested in the SmartHome Light System product. They mentioned several benefits such as remote control, energy-saving, compatibility with other devices, affordability, and a trial period for testing. They also expressed interest in the ease of setup and the idea of controlling lights from their phone. Considering all these factors, I would rate the client's interest in the product at an 8 out of 10.",
    "Sales Pitch Rating": {
        "clarity": {
            "score": "5/10",
            "explanation": "The employee's explanation of the product and its benefits was somewhat clear, but there were instances of hesitancy and lack of specificity."
        },
        "relevance": {
            "score": "6/10",
            "explanation": "The pitch was somewhat relevant to the customer's needs, as the employee highlighted features like remote control and energy-saving capabilities."
        },
        "persuasiveness": {
            "score": "4/10",
            "explanation": "The employee's communication of the product's value lacked strong conviction and enthusiasm, which may have affected persuasiveness."
        },
        "responsiveness": {
            "score": "7/10",
            "explanation": "The employee addressed the customer's questions about the trial period and provided some information on how to get started."
        },
        "overall": {
            "score": "5/10",
            "explanation": "Overall, the sales pitch had room for improvement in terms of clarity, persuasiveness, and relevance, but the employee was responsive to the customer's inquiries."
            }
         }
    }'''
    
    parsed_data = json.loads(json_body)

    order_id = generate_order_id()

    order_text = ("Report Id: " + order_id )
    pdf.add_paragraph(order_text)


    insertIntoPDF(parsed_data, pdf)        
    # Save the PDF
    file_name = order_id + ".pdf"
    pdf.output(file_name)
    print(f"PDF generated and saved as '{file_name}'")

def load_report_count():
    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            return json.load(f)
    return {}

def insertIntoPDF(dictValues, pdfreport) :
    for key, value in dictValues.items() :
        if isinstance(value, dict): 
            pdfreport.add_paragraph(f"{key.capitalize()}:", bold = True, underline = True)
            insertIntoPDF(value, pdfreport)
        else :  
            pdfreport.add_paragraph(f"{key.capitalize()}:", bold = True)
            pdfreport.add_paragraph(f"{value}")


@app.route('/')
def home():
    create_pdf_report()
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
