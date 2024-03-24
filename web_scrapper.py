from bs4 import BeautifulSoup
import requests
import pdfkit


url = "https://www.bahrain.bh/wps/portal/en/BNP/HomeNationalPortal/ContentDetailsPage?current=true&urile=wcm:path:BNP_en/About%20Us/FAQs/FAQs"
response = requests.get(url)
content = response.text

options = {
    'encoding': 'UTF-8'
}


soup = BeautifulSoup(content, 'html.parser')

faqs = soup.find('div', id= 'info', class_= 'section__content')

if faqs:
    qnas = faqs.find_all('p', dir='ltr')

    html_content = ""

    for qna in qnas:
        q_tag = qna.find('strong')

        if q_tag:

            q = q_tag.text.strip()

            a = ''.join([str(item) for item in qna.contents if item.name != 'strong' and item.name != 'span' and item.name != 'br']).strip()

            print('Question: ', q)
            print('Answer: ', a)
            print()

            html_content += f"<p><strong>Question:</strong> {q}</p>"
            html_content += f"<p><strong>Answer:</strong> {a}</p>"
            html_content += f"<br>"

pdf_path = "faq.pdf"

pdfkit.from_string(html_content, pdf_path, options=options)