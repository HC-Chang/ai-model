#    data -> data loader (data, label) -------------------
#                                                        |
# --------------------------------------------------------
# |
# -> model(label, prediction) -> loss function (loss) -> -
#       ^                                                |
#       |--------- optimizer (gradient) <-----------------

from ModelStructure.data.data import Data
from ModelStructure.dataloader.dataloader import DataLoader
from ModelStructure.aimodel.aimodel import AIModel
from ModelStructure.lossfunction.lossfunction import LossFunction
from ModelStructure.optimizer.optimizer import Optizimer


def main():
    data = Data()
    data_loader = DataLoader()
    ai_model = AIModel()
    loss_function = LossFunction()
    optimizer = Optizimer()

    label = "label"
    prediction = "prediction"
    loss = "loss"
    gradient = "gradient"

    data.data1()
    data_loader.data_loader1()
    ai_model.ai_model1(label, prediction)
    loss_function.loss_function1(loss)
    optimizer.optimizer1(gradient)


if __name__ == "__main__":
    main()
