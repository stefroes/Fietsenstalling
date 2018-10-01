# Import QR Code library.
import qrcode


def generate_qr_function():
    """Genereert de QR code en zet deze in een waarde."""

    # Maak de qr code aan.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )

    # De data die je in de QR code wilt stoppen.
    data = "Je fiets code"

    # Voeg de data toe aan de QR code.
    qr.add_data(data)
    qr.make(fit=True)

    # Maak een afbeelding van de QR code informatie.
    img = qr.make_image()

    # Sla de afbeelding ergens op. Verander de extentie naar welk bestandstype je wilt.
    img.save("./QRCodes/image.jpg")
