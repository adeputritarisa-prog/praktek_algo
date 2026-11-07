
import sys
from PyQt5.QtWidgets import *

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Konverter Mata Uang")
        self.setGeometry(300, 300, 350, 250)

        layout = QVBoxLayout()

        # Nilai tukar mata uang ke IDR
        self.rates = {
            "USD (Dolar)": 15500,
            "EUR (Euro)": 16800,
            "SGD (Dolar Singapura)": 11500,
            "JPY (Yen)": 105,
            "IDR (Rupiah)": 1
        }

        # Input jumlah uang
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0, 1000000)
        self.amount_input.setPrefix("Jumlah: ")
        self.amount_input.setDecimals(2)

        # Mata uang asal
        self.from_combo = QComboBox()
        self.from_combo.addItems(self.rates.keys())

        # Mata uang tujuan
        self.to_combo = QComboBox()
        self.to_combo.addItems(self.rates.keys())

        # Label hasil konversi
        self.result_label = QLabel("Hasil: 0")
        self.result_label.setStyleSheet(
            "font-size: 18px; font-weight: bold;"
        )

        # Menambahkan komponen ke layout
        layout.addWidget(QLabel("Konversi Mata Uang"))
        layout.addWidget(self.amount_input)

        layout.addWidget(QLabel("Dari:"))
        layout.addWidget(self.from_combo)

        layout.addWidget(QLabel("Ke:"))
        layout.addWidget(self.to_combo)

        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Menghubungkan sinyal dengan fungsi convert
        self.amount_input.valueChanged.connect(self.convert)
        self.from_combo.currentTextChanged.connect(self.convert)
        self.to_combo.currentTextChanged.connect(self.convert)

        self.convert()

    def convert(self):
        amount = self.amount_input.value()

        from_curr = self.from_combo.currentText()
        to_curr = self.to_combo.currentText()

        # Konversi ke Rupiah terlebih dahulu
        in_idr = amount * self.rates[from_curr]

        # Konversi dari Rupiah ke mata uang tujuan
        result = in_idr / self.rates[to_curr]

        self.result_label.setText(
            f"Hasil: {result:,.2f} {to_curr.split()[0]}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CurrencyConverter()
    window.show()

    sys.exit(app.exec_())
