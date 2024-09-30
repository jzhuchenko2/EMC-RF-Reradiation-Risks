import random
from fpdf import FPDF

def run_emc_simulation():
reradiation_level = round(random.uniform(0.7, 1.2), 2)
snr = round(random.uniform(20, 35), 2)
return reradiation_level, snr

#generating
def generate_report(reradiation_level, snr):
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="EMC Simulation Report", ln=True, align="C")

pdf.cell(200, 10, txt=f"Reradiation Level: {reradiation_level} V/m", ln=False)
pdf.cell(200, 10, txt=f"Signal-to-Noise Ratio (SNR): {snr} dB", ln=True)
compliance = "PASS" if reradiation_level < 1 and snr > 25 else "FALSE"
pdf.cell(200, 10, txt=f"Compliance Status: {compliance}", ln=True)
pdf.output("EMC_Report.pdf")

# Simulate and create report
reradiation, snr = run_emc_simulation()
