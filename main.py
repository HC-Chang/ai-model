#    data -> data loader (data, label) -------------------
#                                                        |
# --------------------------------------------------------
# |
# -> model(label, prediction) -> loss function (loss) -> -
#       ^                                                |
#       |--------- optimizer (gradient) <-----------------

def data():
    pass
def data_loader():
    pass
def model(label, prediction):
    pass
def loss_function(loss):
    pass
def optimizer(gradient):
    pass

def main():
    data()
    data_loader()
    model(label, prediction)
    loss_function(loss)
    optimizer(gradient)



if __name__ == "__main__":
    main()