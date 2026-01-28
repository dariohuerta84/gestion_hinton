### Comenzaré con la creacion de red transformer utilizando 100% python
### Nos vamos a basar en la estrura de la formula QK^T

### Para que ese código de Python se convierta en un Transformer funcional, tendrías que programar estos módulos:

- Clase MultiHeadAttention: Un bucle o una operación matricial que ejecute la función de arriba varias veces.
- Positional Encoding: Una función que genere los valores de sin y cos y los sume a los inputs.
- Capa Feed-Forward: Dos capas densas (Linear) con una activación ReLU en medio.
- Bucle de Entrenamiento: Necesitarías programar el Backpropagation (el cálculo de gradientes) para que la red aprenda.

### El concepto: Fine-tuning vs. Training from scratch
- Training from scratch: Lo que hiciste recién. El modelo empieza de cero. Necesita gigabytes de texto para ser coherente.

- Fine-tuning: El modelo ya leyó internet (GPT-2). Tú solo le das un "repaso" con tus datos. Es mucho más eficiente para datasets pequeños como el tuyo.

EN mi modelo de generador de texto, quiero que sea mas coherente asi que le agregare uin fine tuning para que tenga un conocimiento de por medio, ya que si quiero que aprenda por scratch me tomaria mas tiempo. (como 10 gb de texto xd).