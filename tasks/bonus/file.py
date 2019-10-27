import os
import fpdf
from faker import Faker
import random

fake = Faker()


def descriptions_json(directory, final_directory):
    API_ENDPOINT = "http://localhost:5000/model/predict"
    if final_directory not in os.listdir():
        os.mkdir(final_directory)
    for filename in os.listdir(directory):
        os.system(
            f'curl -F "image=@{directory}/{filename}" -X POST {API_ENDPOINT} >> {final_directory}/{filename}.json')


def parse_responses(output_directory):
    _dict = {}
    for filename in os.listdir(output_directory):
        with open(os.path.join(output_directory, filename), 'r') as file:
            file = (file.readlines()[0])
            file = eval(file)
            strings = []
            for elem in file['predictions']:
                strings.append([elem['caption'], elem['probability']])
            strings.sort(key=lambda x: x[1], reverse=True)
            _dict[filename[:-5]] = strings[0][0]
    return _dict


descriptions_json('final_photos', 'output1')
dicts = []
for elem in ['output1']:
    _dict = parse_responses(elem)
    dicts.append(_dict)


def create_pdf(pics_dirs, strings):
    class PDF(fpdf.FPDF):
        def header(self):
            self.image('logo.png', 10, 10, 33)
            self.set_font('Arial', 'B', 30)
            self.cell(40)
            self.cell(140, 33, 'Apartment for sale!', 1, 0, 'C')
            self.ln(40)

    pdf = PDF()
    for i, pics_dir in enumerate(pics_dirs):
        pdf.add_page()
        pics = os.listdir(pics_dir)
        pdf.set_font('Arial', 'B', 15)
        labels = []
        for pic in pics:
            pdf.set_x(-70)
            pdf.image(f"{pics_dir}/{pic}", w=50, h=40)
            pdf.ln(5)
            labels.append(strings[i][pic])
        pdf.set_y(50)
        pdf.cell(w=80, h=20, txt="We have for sale this amazing apartment,")
        pdf.ln(10)
        pdf.cell(w=80, h=20, txt=f"where You will find {len(pics)} rooms:")
        y = 80
        for string in labels:
            pdf.set_x(10)
            pdf.set_y(y)
            pdf.cell(w=80, h=20, txt=" - " + string)
            pdf.ln(5)
            y += 10
        pdf.ln(15)
        pdf.cell(w=80,h=20, txt="Adress:")
        pdf.ln(10)
        pdf.cell(w=80,h=20, txt=fake.address())
        pdf.ln(10)
        number = "+34 " + str("".join([str(random.randint(1,10)) for _ in range(8)]))
        pdf.cell(w=80,h=20, txt=f"If You are interested contact {fake.name()} ")
        pdf.ln(10)
        pdf.cell(w=80,h=20, txt=f"at {number}")
        pdf.ln(10)
    pdf.output('outcome.pdf', 'F')


create_pdf(['final_photos'], dicts)
