import socket
from des_core import *  # file DES-mu disimpan terpisah sebagai des_core.py

HOST = "0.0.0.0"  # biar bisa diakses dari device lain
PORT = 5555

def server_program():
    print("=== DES Secure Server ===")
    key_input = input("Masukkan key (8 karakter): ")
    if len(key_input) < 8:
        key_input = key_input.ljust(8, '0')

    key_bits = text_to_bits(key_input)
    keys = subkeys(key_bits)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Menunggu koneksi di {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"Terhubung dari {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == "exit":
            print("Client keluar.")
            break

        decrypted = decrypt_ecb(data, keys)
        print(f"[Client] (cipher={data}) → Plaintext: {decrypted}")

        response = input("Balas: ")
        cipher_resp = encrypt_ecb(response, keys)
        conn.send(cipher_resp.encode())

    conn.close()
    print("Koneksi ditutup.")

if __name__ == "__main__":
    server_program()
