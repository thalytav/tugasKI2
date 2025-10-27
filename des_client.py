import socket
from des_core import * 

SERVER_IP = input("Masukkan IP server: ")
PORT = 5555

def client_program():
    print("=== DES Secure Client ===")
    key_input = input("Masukkan key (8 karakter): ")
    if len(key_input) < 8:
        key_input = key_input.ljust(8, '0')

    key_bits = text_to_bits(key_input)
    keys = subkeys(key_bits)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print(f"Terhubung ke server {SERVER_IP}:{PORT}")

    while True:
        msg = input("Kirim pesan: ")
        if msg.lower() == "exit":
            client_socket.send("exit".encode())
            break

        cipher_text = encrypt_ecb(msg, keys)
        client_socket.send(cipher_text.encode())

        data = client_socket.recv(1024).decode()
        if not data:
            break
        decrypted = decrypt_ecb(data, keys)
        print(f"[Server] (cipher={data}) → Plaintext: {decrypted}")

    client_socket.close()
    print("Koneksi ditutup.")

if __name__ == "__main__":
    client_program()

