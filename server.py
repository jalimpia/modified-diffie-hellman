from flask import Flask, render_template, request
import rabinMiller as rm
from flask import jsonify
import datetime as dt
import rsa


#Modified Diffie-Hellman

app = Flask(__name__)

#This will convert bytes data object to int
def toInt(data):
    return int.from_bytes(data, byteorder='big',signed=False)

def toByte(data):
    return data.to_bytes(4096, 'big')


#Load Records from database
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<keysize>/<operation>')
def generateKey(keysize,operation):
    start_time = dt.datetime.now()
    result1 = rm.generateLargePrime(int(keysize))
    if operation=='mult':
        result2=str((result1*2))
    if operation=='div':
        result2=str((result1//2))
    if operation=='none':
        result2=None
    est = dt.datetime.now() - start_time
    return jsonify(result1=str(result1), result2=result2, time=str(est.total_seconds()))

@app.route('/<A>/<B>/<C>')
def generatePublicKey(A,B,C):
    start_time = dt.datetime.now()
    result = pow(int(A),int(B),int(C))
    est = dt.datetime.now() - start_time
    return jsonify(result=str(result), time=str(est.total_seconds()))

@app.route('/rsa/<P>/<Q>/<size>')
def generateRSAKeys(P,Q,size):
    start_time = dt.datetime.now()
    #Generation of e, d, & n
    e, d, n = rsa.generateKey(P,Q,int(size))
    est = dt.datetime.now() - start_time
    return jsonify(E=str(e),D=str(d),N=str(n), time=str(est.total_seconds()))


@app.route('/encrypt/<E>/<N>/<M>')
def encrypt(E,N,M):
    start_time = dt.datetime.now()
    m_bytes = str.encode(M)
    #Encrypting the message
    cipher = pow(toInt(m_bytes),int(E),int(N))
    est = dt.datetime.now() - start_time
    return jsonify(C=str(cipher), time=str(est.total_seconds()))

@app.route('/decrypt/<D>/<N>/<C>')
def decrypt(D,N,C):
    start_time = dt.datetime.now()
    #Encrypting the message
    msg = pow(int(C),int(D),int(N))
    msg = toByte(msg).decode().strip().strip('\x00')
    est = dt.datetime.now() - start_time
    return jsonify(M=str(msg), time=str(est.total_seconds()))

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
