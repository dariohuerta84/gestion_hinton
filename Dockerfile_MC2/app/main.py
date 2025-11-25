import torch
import torch.nn as nn
import torch.optim as optim

def main():

    # Datos simples: y = 3x + 2
    X = torch.unsqueeze(torch.linspace(-5, 5, steps=100), dim=1)
    y = 3 * X + 2

    # Esto define mi red neuronal: 1 capa oculta
    model = nn.Sequential(
        nn.Linear(1, 16),
        nn.ReLU(),
        nn.Linear(16, 1)
    )

    loss_fn = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    print("Pongase serio siervo estamos entrenando un modelo de ML XD")

    # Entrenamiento de mi mente maestra xddd
    for epoch in range(300):
        optimizer.zero_grad()
        pred = model(X)
        loss = loss_fn(pred, y)
        loss.backward()
        optimizer.step()

        if epoch % 50 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

    # Probar el modelo en un dato nuevo:
    test_value = torch.tensor([[4.0]])
    prediction = model(test_value).item()

    print("\nPredicción para x = 4:")
    print(prediction)

if __name__ == "__main__":
    main()
