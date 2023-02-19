#    data -> data loader (data, label) -------------------
#                                                        |
# --------------------------------------------------------
# |
# -> model(label, prediction) -> loss function (loss) -> -
#       ^                                                |
#       |--------- optimizer (gradient) <-----------------

def data():
    print("data")


def data_loader():
    print("data loader")


def model(label, prediction):
    print("model")


def loss_function(loss):
    print("loss function")


def optimizer(gradient):
    print("optimizer")


def main():
    label = "label"
    prediction = "prediction"
    loss = "loss"
    gradient = "gradient"

    data()
    data_loader()
    model(label, prediction)
    loss_function(loss)
    optimizer(gradient)


if __name__ == "__main__":
    main()
