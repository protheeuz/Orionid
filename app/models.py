from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    nim = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Dosen(db.Model):
    __tablename__ = 'dosen'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    nip = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    sks = db.Column(db.Integer, nullable=False)

class Jadwal(db.Model):
    __tablename__ = 'jadwal'
    id = db.Column(db.Integer, primary_key=True)
    mata_kuliah_id = db.Column(db.Integer, db.ForeignKey('mata_kuliah.id'), nullable=False)
    dosen_id = db.Column(db.Integer, db.ForeignKey('dosen.id'), nullable=False)
    ruangan = db.Column(db.String(50), nullable=False)
    waktu = db.Column(db.TIMESTAMP, nullable=False)

    # Relationship
    mata_kuliah = db.relationship('MataKuliah', backref=db.backref('jadwal', lazy=True))
    dosen = db.relationship('Dosen', backref=db.backref('jadwal', lazy=True))

class Tugas(db.Model):
    __tablename__ = 'tugas'
    id = db.Column(db.Integer, primary_key=True)
    mata_kuliah_id = db.Column(db.Integer, db.ForeignKey('mata_kuliah.id'), nullable=False)
    judul = db.Column(db.String(200), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.TIMESTAMP, nullable=False)

    # Relationship
    mata_kuliah = db.relationship('MataKuliah', backref=db.backref('tugas', lazy=True))

class NilaiTugas(db.Model):
    __tablename__ = 'nilai_tugas'
    id = db.Column(db.Integer, primary_key=True)
    tugas_id = db.Column(db.Integer, db.ForeignKey('tugas.id'), nullable=False)
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey('mahasiswa.id'), nullable=False)
    nilai = db.Column(db.Integer, nullable=False)

    # Relationship
    tugas = db.relationship('Tugas', backref=db.backref('nilai_tugas', lazy=True))
    mahasiswa = db.relationship('Mahasiswa', backref=db.backref('nilai_tugas', lazy=True))
