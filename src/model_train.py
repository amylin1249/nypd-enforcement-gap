from sklearn.model_selection import train_test_split

# X(feature), y(target) split
train_x, test_x, train_y, test_y = train_test_split(
    X, y, test_size=0.2, random_state=123
)