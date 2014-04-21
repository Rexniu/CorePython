#????????
def subchr(string,origchar,newchar):
  output = ''
  for i in origchar:
    if i == string:
      output = output + newchar
    else:
      output = output + i
  print output

subchr('c','abdskfasdfd','k')

