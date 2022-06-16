import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC

def train_model():
    df = pd.read_csv('emotions.csv')

    # Applying Standard Scaler
    scalar = StandardScaler()
    scalar.fit(df.drop("label", axis=1)) 

    # dropping the last 'label' column
    scaled_data = scalar.transform(df.drop("label", axis=1))

    # Applying Principal Component Analysis to reduce dimensions
    pca = PCA(0.98)
    pca.fit(scaled_data)
    reduced_data = pca.transform(scaled_data)

    df2 = pd.DataFrame(reduced_data)

    # Spliting the dataset for traing and testing
    x_train, x_test, y_train, y_test = train_test_split(df2,df.label, test_size=0.3)

    # Training the model using Support Vector Machine
    model = SVC(C = 10)
    model.fit(x_train,y_train)

    # print(type(model.fit(x_train,y_train)))

    # Calculating the accuracy
    accuracy_of_model = model.score(x_test, y_test)
    # print(accuracy_of_model)

    # Evaluating User Report
    user_health = model.predict(df2.head(1))
    # print(user_health)

    return (user_health[0], accuracy_of_model, model)


# print(train_model())

def test(file_path):
    user_df = pd.read_csv(file_path)
    training_data = train_model()
    m = training_data[2]
    user_health =  m.predict(user_df)
    return (user_health[0], training_data[1])
