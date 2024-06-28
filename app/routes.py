from flask import Flask, jsonify, request
from app import app, db
from .models import Mahasiswa

@app.route('/mahasiswa', methods=['GET'])
def get_mahasiswa():
    mahasiswa_list = Mahasiswa.query.all()
    return jsonify([mhs.nama for mhs in mahasiswa_list])

@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    data = request.get_json()
    new_mahasiswa = Mahasiswa(nama=data['nama'], nim=data['nim'], email=data['email'], password=data['password'])
    db.session.add(new_mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa berhasil ditambahkan'}), 201