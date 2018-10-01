import tempfile



tf = tempfile.TemporaryFile()
tf.write(b'Hello world!')
tf.seek(0)
print(tf.read())
tf.close()



ntf = tempfile.NamedTemporaryFile()

print(ntf.name)

ntf.close()


with tempfile.NamedTemporaryFile() as ntf:
    print(ntf.name)
    ntf.write(b'hello')
    ntf.seek(0)
    print(ntf.read())
    
    
    
