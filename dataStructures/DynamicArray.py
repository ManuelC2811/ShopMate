import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Indice fuera de rango")
        return self._A[k]

    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self,c):
        return (c*ctypes.py_object)()

    def is_empty(self):
        return self._n == 0
    
    def delete(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Índice fuera de rango")
        
        # Desplazar los elementos hacia la izquierda desde la posición k hasta el final
        for i in range(k, self._n - 1):
            self._A[i] = self._A[i + 1]
        
        # Decrementar el tamaño del arreglo
        self._n -= 1

        # Si el tamaño del arreglo es menor que la mitad de la capacidad, reducir la capacidad
        if self._n < self._capacity // 2:
            self._resize(self._capacity // 2)

    def set_item(self, k, obj):
        if not 0 <= k < self._n:
            raise IndexError("Índice fuera de rango")
        
        # Establecer el valor del elemento en la posición k
        self._A[k] = obj

       