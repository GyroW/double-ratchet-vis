import tkinter as tk
import textwrap
import time

my_wrap = textwrap.TextWrapper(width = 40)

ROWSIZE = 30


last = {}
last["dh"] = 0
last["root"] = 0
last["send"] = 0
last["receive"] = 0

blast = {}
blast["dh"] = 0
blast["root"] = 0
blast["send"] = 0
blast["receive"] = 0
mws = tk.Tk()




EXPL_ROOTKEY="This is a key in the root chain, this key is synchronised between Alice and Bob. When receiving a public key from the other party or when sending a message with a new public key, a Diffie-Hellman exchange is performed, the output from this exchange, together with the root chain key is fed to a KDF from which a new root chain key and new receive or send chain key respectively is generated. The old (above) root chain keys need to be deleted to provide forward secrecy."
EXPL_SENDCHAINKEY="This is a chain key in the send chain. Whenever a new message is sent this chain key gets fed to a KDF, producing a new chain key and a message key. This message key is used to encrypt the new message. The old (above) sending chain keys need to be deleted to provide forward secrecy."
EXPL_SENDMESSAGEKEY="This is a message key in the send chain. Whenever a new message is sent a new key gets generated to encrypt said new single message." 

EXPL_RECVCHAINKEY="This is a chain key in the receive chain. Whenever a new message is received this chain key gets fed to a KDF, producing a new chain key and a message key. This message key is used decrypt the newly received message. The old (above) receiving chain keys need to be deleted to provide forward secrecy."
EXPL_RECVMESSAGEKEY="This is a message key in the receive chain. Whenever a new message is received a new key gets generated to decrypt the received single message." 

EXPL_KDF="This is a KDF or Key Derivation Function, given a key and some input it generates a two new keys."
EXPL_DH="This is a Diffie-Hellman key exchange, given a public key of the other party and own private key, a value can be calculated. The other party will be able to calculate the same value using their private key and the sent public key."

EXPL_RECVPUBKEY="This is a public key received from the other party. It will be used in conjuction with the own private key to perform a Diffie-Hellman key exchange."
EXPL_SENTPUBKEY="This is a public key sent to the other party. It will be used in conjuction with the private key of the other party to perform a Diffie-Hellman key exchange."
EXPL_PRIVKEY="This is a private key to be used with a public key received from the other party to perform a Diffie-Hellman key exchange."

EXPLANATIONS = dict()
#' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(<++>, width=40))])
EXPLANATIONS["EXPL_ROOTKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_ROOTKEY, width=40))])
EXPLANATIONS["EXPL_SENDCHAINKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_SENDCHAINKEY, width=40))])
EXPLANATIONS["EXPL_SENDMESSAGEKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_SENDMESSAGEKEY, width=40))])
EXPLANATIONS["EXPL_RECVCHAINKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_RECVCHAINKEY, width=40))])
EXPLANATIONS["EXPL_RECVMESSAGEKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_RECVMESSAGEKEY, width=40))])
EXPLANATIONS["EXPL_KDF"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_KDF, width=40))])
EXPLANATIONS["EXPL_DH"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_DH, width=40))])
EXPLANATIONS["EXPL_RECVPUBKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_RECVPUBKEY, width=40))])
EXPLANATIONS["EXPL_SENTPUBKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_SENTPUBKEY, width=40))])
EXPLANATIONS["EXPL_PRIVKEY"] = ' '.join([str(elem) for elem in map(( lambda x: x+'\n'),textwrap.wrap(EXPL_PRIVKEY, width=40))])

def enter(event):
    a = canvas.gettags("current")
    if len(a) > 0:
        canvas.itemconfigure(key, text=EXPLANATIONS[a[0]])
    b = bcanvas.gettags("current")
    if len(b) > 0:
        bcanvas.itemconfigure(bkey, text=EXPLANATIONS[b[0]])

def draw_dh(cv, column, row):
    x = 120+column*240
    y = 50+row*ROWSIZE
    r = 10
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    obj = cv.create_oval(x0, y0, x1, y1, fill ="#858585", tags="EXPL_DH")
    
    cv.tag_bind(obj, '<1>', enter)
    #cv.tag_bind(obj, '<Leave>', leave)

    obj = cv.create_text(x, y+2, text="DH", font=('Helvetica 7 bold'), tags="EXPL_DH")
    cv.tag_bind(obj, '<1>', enter)
    #cv.tag_bind(obj, '<Leave>', leave)

def draw_kdf(cv, column, row):
    r = 10
    x = 120+column*240
    y = 50+row*ROWSIZE
    x0 = x - r
    y0 = y + r
    x1 = x + r
    y1 = y - r
    obj = cv.create_rectangle(x0, y0, x1, y1, fill="#858585", tags="EXPL_KDF")
    cv.tag_bind(obj, '<1>', enter)
    obj = cv.create_text(x, y+2, text="KDF", font=('Helvetica 7 bold'), tags="EXPL_KDF")
    cv.tag_bind(obj, '<1>', enter)

def draw_pubk(cv, column, row, arrow=False, color="#006664", text="", tag="pubk"):
    #width of these things is 40
    offset = 20
    item = cv.create_polygon(  120+column*240, offset+40+row*ROWSIZE, 100+column*240,  offset+40+row*ROWSIZE, 90+column*240,  offset+30+row*ROWSIZE, 100+column*240,  offset+20+row*ROWSIZE, 140+column*240, offset+20+row*ROWSIZE, 140+column*240, offset+40+row*ROWSIZE, 120+column*240, offset+40+row*ROWSIZE, fill=color, tags=tag)
    cv.tag_bind(item, '<1>', enter)

    obj = cv.create_text(120+column*240, 50+row*ROWSIZE+2, text=text, font=('Helvetica 7 bold'), tags=tag)
    cv.tag_bind(obj, '<1>', enter)

    if arrow:
        cv.create_line( 180+column*240, offset+30+row*ROWSIZE,
                        140+column*240, offset+30+row*ROWSIZE,
                        arrow=tk.LAST)

def draw_privk(cv, column, row, color="#FFC745", text="", tag="privk"):
    offset = 20
    obj = cv.create_polygon(  140+column*240, offset+40+row*ROWSIZE, 180+column*240, offset+40+row*ROWSIZE, 190+column*240, offset+30+row*ROWSIZE, 180+column*240, offset+20+row*ROWSIZE, 140+column*240, offset+20+row*ROWSIZE, 140+column*240, offset+40+row*ROWSIZE, fill=color, tags=tag)
    cv.tag_bind(obj, '<1>', enter)

    obj = cv.create_text(120+40+column*240, 50+row*ROWSIZE+2, text=text, font=('Helvetica 7 bold'), tags=tag)
    cv.tag_bind(obj, '<1>', enter)

def draw_pair(cv, column, row, pubtag="EXPL_SENTPUBKEY", privtag="EXPL_PRIVKEY", text=""):
    draw_pubk(cv, column, row, False, color="#FFC745", text=text, tag=privtag)
    draw_privk(cv, column, row, color="#006664", text=text, tag=pubtag)


def draw_key(cv, column, row, text="", tag="key"):
    offset = 20
    obj = cv.create_polygon(  120+column*240, offset+40+row*ROWSIZE, 100+column*240,  offset+40+row*ROWSIZE, 90+column*240,  offset+30+row*ROWSIZE, 100+column*240,  offset+20+row*ROWSIZE, 140+column*240, offset+20+row*ROWSIZE, 150+column*240, offset+30+row*ROWSIZE, 140+column*240, offset+40+row*ROWSIZE, 120+column*240, offset+40+row*ROWSIZE, fill="#B5101E", tags=tag)

    cv.tag_bind(obj, '<1>', enter)
    obj = cv.create_text(120+column*240, 50+row*ROWSIZE+2, text=text, font=('Helvetica 7 bold'), tags=tag)
    cv.tag_bind(obj, '<1>', enter)


def draw_cross(cv, column, row):
    obj = cv.create_line(80+column*240, 40+row*ROWSIZE, 160+column*240, 60+row*ROWSIZE)
    obj = cv.create_line(80+column*240, 60+row*ROWSIZE, 160+column*240, 40+row*ROWSIZE)





#### END PRIMITIVES ####


#chain key and a send message key
def advance_send_ratchet_bob(cv, row, dlast, textkey=""):
    draw_kdf(cv, 2.75, row+1)
    draw_key(cv, 2.75, row+2, text="CK", tag="EXPL_SENDCHAINKEY")
    draw_key(cv, 3.25, row+2, text=textkey, tag="EXPL_SENDMESSAGEKEY")

    #last chain_key - > kdf
    cv.create_line(120+240*2.75, 60+dlast["send"]*ROWSIZE, 120+240*2.75, 40+(row+1)*ROWSIZE)
    # kdf -> new chain key
    cv.create_line(120+240*2.75, 60+(row+1)*ROWSIZE, 120+240*2.75, 40+(row+2)*ROWSIZE)
    # kdf -> new message key
    cv.create_line( 120+240*2.75, 95+(row)*ROWSIZE, 120+240*3.25, 95+(row)*ROWSIZE, 120+240*3.25, 100+(row)*ROWSIZE)


    dlast["send"] = row+2
    return row+2


# This needs a a root key, a public/private keypair, a chain key, (a second chain key and a send message key) for the advance_send ratchet
def send_msg_with_new_key_bob(cv, row, dlast, textpair="", textsendkey=""):
    draw_dh(cv, 0, row+1) 
    draw_kdf(cv, 1, row+1) 
    draw_pair(cv, 0, row+2, text=textpair) 
    cv.create_line(120+70, 50+(row+2)*ROWSIZE, 120+100, 50+(row+2)*ROWSIZE, arrow=tk.LAST)
    draw_key(cv, 1, row+2, text="RK", tag="EXPL_ROOTKEY")
    draw_key(cv, 2.75, row+2, text="CK", tag="EXPL_SENDCHAINKEY")

    #last pub key -> dh
    cv.create_line( 120+240*0, 60+dlast["dh"]*ROWSIZE, 120+240*0, 40+(row+1)*ROWSIZE)
    # last root -> kdf
    cv.create_line( 120+240*1, 60+dlast["root"]*ROWSIZE, 120+240*1, 40+(row+1)*ROWSIZE)
    #dh -> new priv key
    cv.create_line( 120+240*0, 60+(row+1)*ROWSIZE, 120+240*0, 40+(row+2)*ROWSIZE)
    #kdf -> new root key
    cv.create_line( 120+240*1, 60+(row+1)*ROWSIZE, 120+240*1, 40+(row+2)*ROWSIZE)
    #dh -> kdf
    cv.create_line( 120+10, 80+(row)*ROWSIZE, 120-10+240, 80+(row)*ROWSIZE, arrow=tk.LAST)

    #kdf -> ck
    cv.create_line( 120+240*1, 95+(row)*ROWSIZE, 120+240*2.75, 95+(row)*ROWSIZE, 120+240*2.75, 100+(row)*ROWSIZE)


    dlast["dh"] = row+2
    dlast["send"] = row+2
    dlast["root"] = row+2

    row = advance_send_ratchet_bob(cv, row+2, dlast=dlast, textkey=textsendkey)
    return row
# this needs a chain key and a receive message key
def advance_rcv_ratchet_alice(cv, row, dlast, textkey="", new=False):
    draw_kdf(cv, 2.75, row+1)
    draw_key(cv, 2.75, row+2, text="CK", tag="EXPL_RECVCHAINKEY")
    draw_key(cv, 3.25, row+2, text=textkey, tag="EXPL_RECVMESSAGEKEY")

    #last chain_key - > kdf
    cv.create_line(120+240*2.75, 60+dlast["receive"]*ROWSIZE, 120+240*2.75, 40+(row+1)*ROWSIZE)
    # kdf -> new chain key
    cv.create_line(120+240*2.75, 60+(row+1)*ROWSIZE, 120+240*2.75, 40+(row+2)*ROWSIZE)
    # kdf -> new message key
    cv.create_line( 120+240*2.75, 95+(row)*ROWSIZE, 120+240*3.25, 95+(row)*ROWSIZE, 120+240*3.25, 100+(row)*ROWSIZE)



    dlast["receive"] = row+2
    return row+2

# This needs a public key, a root key and a chain key (chain key and receive message key) for advance_rcv_ratchet
def rcv_msg_with_new_key_alice(cv, row, dlast, textpub="", textrcvkey=""):
    draw_pubk(cv, 0, row+2, arrow=True, text=textpub, tag="EXPL_RECVPUBKEY")
    draw_dh(cv, 0, row+1)
    draw_kdf(cv, 1, row+1)
    draw_key(cv, 1, row+2, text="RK", tag="EXPL_ROOTKEY")
    draw_key(cv, 2.75, row+2, text="CK", tag="EXPL_RECVCHAINKEY")

    #last pub key -> dh
    cv.create_line( 120+240*0, 60+dlast["dh"]*ROWSIZE, 120+240*0, 40+(row+1)*ROWSIZE)
    # last root -> kdf
    cv.create_line( 120+240*1, 60+dlast["root"]*ROWSIZE, 120+240*1, 40+(row+1)*ROWSIZE)
    #dh -> new priv key
    cv.create_line( 120+240*0, 60+(row+1)*ROWSIZE, 120+240*0, 40+(row+2)*ROWSIZE)
    #kdf -> new root key
    cv.create_line( 120+240*1, 60+(row+1)*ROWSIZE, 120+240*1, 40+(row+2)*ROWSIZE)
    #dh -> kdf
    cv.create_line( 120+10, 80+(row)*ROWSIZE, 120-10+240, 80+(row)*ROWSIZE, arrow=tk.LAST)

    #kdf -> ck
    cv.create_line( 120+240*1, 95+(row)*ROWSIZE, 120+240*2.75, 95+(row)*ROWSIZE, 120+240*2.75, 100+(row)*ROWSIZE)

    dlast["dh"] = row+2
    dlast["receive"] = row+2
    dlast["root"] = row+2



    row = advance_rcv_ratchet_alice(cv, row+2, dlast=dlast, textkey=textrcvkey)
    return row

# see above
def advance_send_ratchet_alice(cv, row, dlast, textkey=""):
    draw_kdf(cv, 1.75, row+1)
    draw_key(cv, 1.75, row+2, text="CK", tag="EXPL_SENDCHAINKEY")
    draw_key(cv, 2.25, row+2, text=textkey, tag="EXPL_SENDMESSAGEKEY")

    #last chain_key - > kdf
    cv.create_line(120+240*1.75, 60+dlast["send"]*ROWSIZE, 120+240*1.75, 40+(row+1)*ROWSIZE)
    # kdf -> new chain key
    cv.create_line(120+240*1.75, 60+(row+1)*ROWSIZE, 120+240*1.75, 40+(row+2)*ROWSIZE)
    # kdf -> new message key
    cv.create_line( 120+240*1.75, 95+(row)*ROWSIZE, 120+240*2.25, 95+(row)*ROWSIZE, 120+240*2.25, 100+(row)*ROWSIZE)


    dlast["send"] = row+2
    return row+2

def send_msg_with_new_key_alice(cv, row, dlast, textpair="", textsendkey=""):
    draw_dh(cv, 0, row+1) 
    draw_kdf(cv, 1, row+1) 
    draw_pair(cv, 0, row+2, text=textpair) 
    cv.create_line(120+70, 50+(row+2)*ROWSIZE, 120+100, 50+(row+2)*ROWSIZE, arrow=tk.LAST)
    draw_key(cv, 1, row+2, text="RK", tag="EXPL_ROOTKEY")
    draw_key(cv, 1.75, row+2, text="CK", tag="EXPL_SENDCHAINKEY")

    #last pub key -> dh
    cv.create_line( 120+240*0, 60+dlast["dh"]*ROWSIZE, 120+240*0, 40+(row+1)*ROWSIZE)
    # last root -> kdf
    cv.create_line( 120+240*1, 60+dlast["root"]*ROWSIZE, 120+240*1, 40+(row+1)*ROWSIZE)
    #dh -> new priv key
    cv.create_line( 120+240*0, 60+(row+1)*ROWSIZE, 120+240*0, 40+(row+2)*ROWSIZE)
    #kdf -> new root key
    cv.create_line( 120+240*1, 60+(row+1)*ROWSIZE, 120+240*1, 40+(row+2)*ROWSIZE)
    #dh -> kdf
    cv.create_line( 120+10, 80+(row)*ROWSIZE, 120-10+240, 80+(row)*ROWSIZE, arrow=tk.LAST)

    #kdf -> ck
    cv.create_line( 120+240*1, 95+(row)*ROWSIZE, 120+240*1.75, 95+(row)*ROWSIZE, 120+240*1.75, 100+(row)*ROWSIZE)


    dlast["dh"] = row+2
    dlast["send"] = row+2
    dlast["root"] = row+2

    row = advance_send_ratchet_alice(cv, row+2, dlast=dlast, textkey=textsendkey)
    return row

def advance_rcv_ratchet_bob(cv, row, dlast, textkey=""):
    draw_kdf(cv, 1.75, row+1)
    draw_key(cv, 1.75, row+2, text="CK" ,tag="EXPL_RECVCHAINKEY")
    draw_key(cv, 2.25, row+2, text=textkey, tag="EXPL_RECVMESSAGEKEY")

    #last chain_key - > kdf
    cv.create_line(120+240*1.75, 60+dlast["receive"]*ROWSIZE, 120+240*1.75, 40+(row+1)*ROWSIZE)
    # kdf -> new chain key
    cv.create_line(120+240*1.75, 60+(row+1)*ROWSIZE, 120+240*1.75, 40+(row+2)*ROWSIZE)
    # kdf -> new message key
    cv.create_line( 120+240*1.75, 95+(row)*ROWSIZE, 120+240*2.25, 95+(row)*ROWSIZE, 120+240*2.25, 100+(row)*ROWSIZE)


    dlast["receive"] = row+2
    return row+2

def rcv_msg_with_new_key_bob(cv, row, dlast, textpub="", textrcvkey=""):
    draw_pubk(cv, 0, row+2, arrow=True, text=textpub, tag="EXPL_RECVPUBKEY")
    draw_dh(cv, 0, row+1)
    draw_kdf(cv, 1, row+1)
    draw_key(cv, 1, row+2, text="RK", tag="EXPL_ROOTKEY")
    draw_key(cv, 1.75, row+2, text="CK", tag="EXPL_RECVCHAINKEY")

    #last pub key -> dh
    cv.create_line( 120+240*0, 60+dlast["dh"]*ROWSIZE, 120+240*0, 40+(row+1)*ROWSIZE)
    # last root -> kdf
    cv.create_line( 120+240*1, 60+dlast["root"]*ROWSIZE, 120+240*1, 40+(row+1)*ROWSIZE)
    #dh -> new priv key
    cv.create_line( 120+240*0, 60+(row+1)*ROWSIZE, 120+240*0, 40+(row+2)*ROWSIZE)
    #kdf -> new root key
    cv.create_line( 120+240*1, 60+(row+1)*ROWSIZE, 120+240*1, 40+(row+2)*ROWSIZE)
    #dh -> kdf
    cv.create_line( 120+10, 80+(row)*ROWSIZE, 120-10+240, 80+(row)*ROWSIZE, arrow=tk.LAST)

    #kdf -> ck
    cv.create_line( 120+240*1, 95+(row)*ROWSIZE, 120+240*1.75, 95+(row)*ROWSIZE, 120+240*1.75, 100+(row)*ROWSIZE)

    dlast["dh"] = row+2
    dlast["receive"] = row+2
    dlast["root"] = row+2

    row = advance_rcv_ratchet_bob(cv, row+2, dlast=dlast, textkey=textrcvkey)
    return row

def init_alice(cv, row, dlast):
    cv.create_text(20, 20, text="Alice", font=('Helvetica 10 bold'))
    cv.create_text(120, 20, text="Ratchet", font=('Helvetica 10 bold'))
    cv.create_text(120+240, 20, text="Root", font=('Helvetica 10 bold'))
    cv.create_text(120+2*240, 20, text="Send", font=('Helvetica 10 bold'))
    cv.create_text(120+3*240, 20, text="Receive", font=('Helvetica 10 bold'))
    draw_pubk(cv, 0, row, arrow=True, text="B0",tag="EXPL_RECVPUBKEY")
    draw_key(cv, 1, row, text="RK", tag="EXPL_ROOTKEY")
    return row


def init_bob(cv, row, dlast):
    cv.create_text(20, 20, text="Bob", font=('Helvetica 10 bold'))
    cv.create_text(120, 20, text="Ratchet", font=('Helvetica 10 bold'))
    cv.create_text(120+240, 20, text="Root", font=('Helvetica 10 bold'))
    cv.create_text(120+2*240, 20, text="Receive", font=('Helvetica 10 bold'))
    cv.create_text(120+3*240, 20, text="Send", font=('Helvetica 10 bold'))
    draw_pair(cv, 0, row, text="B0")
    draw_key(cv, 1, row, text="RK", tag="EXPL_ROOTKEY")
    return row

ws = tk.Tk()
ws.title('Alice')
frame = tk.Frame( ws, width=1280, height=1080)
frame.pack(expand=True, fill=tk.BOTH)
canvas=tk.Canvas( frame, bg='white', width=1280, height=1000, scrollregion=(0,0,1080,2000))
vertibar=tk.Scrollbar( frame, orient=tk.VERTICAL)
vertibar.pack(side=tk.RIGHT,fill=tk.Y)
vertibar.config(command=canvas.yview)
canvas.config(width=1280,height=1000)
canvas.config( yscrollcommand=vertibar.set)
canvas.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)

bws = tk.Tk()
bws.title('Bob')
bframe = tk.Frame( bws, width=1280, height=1080)
bframe.pack(expand=True, fill=tk.BOTH)
bcanvas=tk.Canvas( bframe, bg='white', width=1280, height=1000, scrollregion=(0,0,1080,2000))
bvertibar=tk.Scrollbar( bframe, orient=tk.VERTICAL)
bvertibar.pack(side=tk.RIGHT,fill=tk.Y)
bvertibar.config(command=bcanvas.yview)
bcanvas.config(width=1280,height=1000)
bcanvas.config( yscrollcommand=bvertibar.set)
bcanvas.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)

canvas.create_text(80+4*240, 20, text="Explanation", font=('Helvetica 10 bold'))
key = canvas.create_text(80+4*240, 40, text="", font=('Helvetica 10 bold'), anchor="n")
bcanvas.create_text(80+4*240, 20, text="Explanation", font=('Helvetica 10 bold'))
bkey = bcanvas.create_text(80+4*240, 40, text="", font=('Helvetica 10 bold'), anchor="n")


counter = 1
bcounter = 1
c_row = 0
bc_row = 0
state = 0

c_row = init_alice(canvas, c_row, dlast=last)
bc_row = init_bob(bcanvas, bc_row, dlast=last)

#c_row = send_msg_with_new_key_alice(canvas, c_row, dlast=last, textpair="A"+str(counter), textsendkey="A"+str(counter))
#bc_row = rcv_msg_with_new_key_bob(bcanvas, bc_row, dlast=blast, textpub="A"+str(counter), textrcvkey="A"+str(counter))
#counter+=1
#
#while True:
#    a = input()
#    if a == "exit":
#        exit()
#
#
#    # Bob sends message with new key
#    elif a == "c":
#        if state == 0 or state == 2:
#            bc_row = send_msg_with_new_key_bob(bcanvas, bc_row, dlast=blast, textpair="B"+str(bcounter), textsendkey="B"+str(bcounter))
#            c_row = rcv_msg_with_new_key_alice(canvas, c_row, dlast=last, textpub="B"+str(bcounter), textrcvkey="B"+str(bcounter))
#            bcounter+=1
#            state = 1
#        else:
#            print("ILLEGAL")
#
#    # Bob sends message with old key
#    elif a == "d":
#        if state == 1 or state == 2:
#            bc_row = advance_send_ratchet_bob(bcanvas, bc_row, dlast=blast, textkey="B"+str(bcounter))
#            c_row = advance_rcv_ratchet_alice(canvas, c_row, dlast=last, textkey="B"+str(bcounter))
#            bcounter+=1
#        else:
#            print("ILLEGAL")
#
#    # Alice sends message with new key
#    elif a == "e":
#        if state == 1:
#            c_row = send_msg_with_new_key_alice(canvas, c_row, dlast=last, textpair="A"+str(counter), textsendkey="A"+str(counter))
#            bc_row = rcv_msg_with_new_key_bob(bcanvas, bc_row, dlast=blast, textpub="A"+str(counter), textrcvkey="A"+str(counter))
#            counter+=1
#            state = 2
#        else: 
#            print("ILLEGAL")
#
#    # Alice sends message with old key
#    elif a == "f":
#        c_row = advance_send_ratchet_alice(canvas, c_row, dlast=last, textkey="A"+str(counter))
#        bc_row = advance_rcv_ratchet_bob(bcanvas, bc_row, dlast=blast, textkey="A"+str(counter))
#        counter+=1


def do_c(state):
    global bcounter
    global c_row
    global bc_row
    if state in [1,3]:

        # Gather and do cryptostuff here!


        bc_row = send_msg_with_new_key_bob(bcanvas, bc_row, dlast=blast, textpair="B"+str(bcounter), textsendkey="B"+str(bcounter))
        c_row = rcv_msg_with_new_key_alice(canvas, c_row, dlast=last, textpub="B"+str(bcounter), textrcvkey="B"+str(bcounter))



        bcounter+=1
        state = 2
    else:
        return -1
    return state

def do_d(state):
    global bcounter
    global c_row
    global bc_row
    if state in [2,3]:

        # Gather and do cryptostuff here!


        bc_row = advance_send_ratchet_bob(bcanvas, bc_row, dlast=blast, textkey="B"+str(bcounter))
        c_row = advance_rcv_ratchet_alice(canvas, c_row, dlast=last, textkey="B"+str(bcounter), new=True)
        bcounter+=1
    else:
        return -1
    return state

def do_e(state):
    global counter
    global c_row
    global bc_row
    if state in [0,2]:

        # Gather and do cryptostuff here!


        c_row = send_msg_with_new_key_alice(canvas, c_row, dlast=last, textpair="A"+str(counter), textsendkey="A"+str(counter))
        bc_row = rcv_msg_with_new_key_bob(bcanvas, bc_row, dlast=blast, textpub="A"+str(counter), textrcvkey="A"+str(counter))
        counter+=1
        state += 1
    else: 
        return -1
    return state

def do_f(state):
    global counter
    global c_row
    global bc_row
    if state in [1,2,3]:

        # Gather and do cryptostuff here!


        c_row = advance_send_ratchet_alice(canvas, c_row, dlast=last, textkey="A"+str(counter))
        bc_row = advance_rcv_ratchet_bob(bcanvas, bc_row, dlast=blast, textkey="A"+str(counter))
        counter+=1
    else:
        return -1
    return state

mws.configure(bg='white')
mws.title('Messages')

def send_as_alice(event=None):
    global state
    oldstate = state
    if state == 0:
        state = do_e(state)

    elif avar.get(): #prefer new key
        state = do_e(state)
        if state == -1:
            state = do_f(oldstate)
            
    else:
        state = do_f(state)

    if state == -1:
        state = oldstate
    else:
        tk.Label(frame, text="Alice (A"+str(counter-1)+"):"+a.get(), bg='white', fg='black').pack()
        a.delete(0, 'end')

def send_as_bob(event=None):
    global state
    oldstate = state
    if state == 1:
        state = do_c(state)
    
    elif bvar.get():
        state = do_c(state)
        if state == -1:
            state = do_d(oldstate)
    else:
        state = do_d(state)

    if state == -1:
        state = oldstate
    else:
        tk.Label(frame, text="Bob(B"+str(bcounter-1)+"):"+b.get(), bg='white', fg='black').pack()
        b.delete(0, 'end')

frame = tk.Frame(mws, bg='white')
frame.grid(row=2, column=0)
tk.Label(mws, text="Send message as Alice:", bg='white', fg='black').grid(row=0)
tk.Label(mws, text="Send message as Bob:", bg='white', fg='black').grid(row=1)
alice = tk.Button(mws, text = "Send", command=send_as_alice, bg='white', fg='black').grid(row=0, column=2)
bob = tk.Button(mws, text = "Send", command=send_as_bob, bg='white', fg='black').grid(row=1, column=2)
a = tk.Entry(mws, bg='white', fg='black')
a.bind('<Return>', send_as_alice)
b = tk.Entry(mws, bg='white', fg='black')
b.bind('<Return>', send_as_bob)
a.grid(row=0, column=1)
b.grid(row=1, column=1)


avar=tk.IntVar()
bvar=tk.IntVar()
avar.set(1)
bvar.set(1)
ac = tk.Checkbutton(mws, text='Prefer new key',variable=avar, onvalue=1, offvalue=0,fg='black', bg='white')
bc = tk.Checkbutton(mws, text='Prefer new key',variable=bvar, onvalue=1, offvalue=0,fg='black', bg='white')
ac.select()
bc.select()

ac.grid(row=0, column=3)
bc.grid(row=1, column=3)

mws.mainloop()
