# QR-Steganography
This rep is QR code steganography, hidden QR code to a normal picture

---
# Install Dependence
```bash
$ conda create -n qr_ste python=3.10
$ conda activate qr_ste
```

After create, install dependence packages:
```bash
$ pip install qrcode
$ pip install Pillow
```

---
# How to use

## Step1. Prepare a carrier image
you need to prepare at least one carrier image, in this rep is 'carrier.png'.

## Step2. [Optional] Prepare a QR code
this step is optional, if you wanna use yourself QR code, you can skip this step.

[Note]: Carrier image must BIGGER than QR code in pixel size;

you can also use this command to generate a QR code, saved as 'my_qrcode.png'

```bash
(qr_ste) $ python generate.py
```

## Step3. Hide the QR code
use this command to hide the QR code inside carrier image BLUE channel.

```bash
(qr_ste) $ python hidden.py
```

'output.png' will generate.

## Step4. Extract QR code
use this command to extract QR code from 'output.png'.

```bash
(qr_ste) $ python parase.py
```

'extracted_qr.png' will generate.
