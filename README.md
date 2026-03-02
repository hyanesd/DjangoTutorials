# DjangoTutorials

## Screenshots

## Tutorial 1 
### Home
<img width="1470" height="956" alt="home" src="https://github.com/user-attachments/assets/33e493b9-dd58-44a7-b201-93050c5d1df2" />

### About
<img width="1470" height="956" alt="1" src="https://github.com/user-attachments/assets/0706e2f5-349b-48dc-9941-bbe5a522b8ef" />

### Product Information
<img width="1470" height="956" alt="2" src="https://github.com/user-attachments/assets/e9d242bc-28fb-4d8b-8ca8-dfd9512f3599" />

### Create Product
<img width="1470" height="956" alt="3" src="https://github.com/user-attachments/assets/bf0e2d15-1836-49c6-a306-2a1015a77b27" />

### Price validation
<img width="1470" height="956" alt="4" src="https://github.com/user-attachments/assets/01848789-dc60-4fb5-9c3b-720d90eaf81b" />

### Product created
<img width="1470" height="956" alt="5" src="https://github.com/user-attachments/assets/875d550c-3c68-4c2e-ad77-11776e4791f4" />

## Tutorial 2
### Products
<img width="1470" height="956" alt="products" src="https://github.com/user-attachments/assets/a52a7993-6009-43b1-88a0-9cf37140722e" />

### Data base 
<img width="1117" height="547" alt="bd1" src="https://github.com/user-attachments/assets/e688f9e5-8b0b-4fe5-aa98-4283be8816a4" />
<img width="1217" height="545" alt="bd2" src="https://github.com/user-attachments/assets/5ad12847-5035-43fa-b892-66884ca08eb5" />

## Tutorial 3 
### Cart 
<img width="1470" height="956" alt="cart" src="https://github.com/user-attachments/assets/bec0be33-122a-46ba-8688-c6c93660ed3d" />

### Upload image
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/47153a14-fc22-4656-9370-51ea85c4c03e" />

### Preguntas 
1. ¿Puedes entender las diferencias entre las dos propuestas?
- Sí, entiendo la diferencia, aunque las dos versiones hacen lo mismo, en la versión con DI la vista no crea directamente la clase que guarda la imagen sino que la recibe desde afuera; en la versión sin DI la vista crea esa clase directamente. Entonces la diferencia no es lo que hace el programa, sino cómo está organizado.

2. ¿Ventajas/desventajas de cada una?
- La versión con DI es más flexible porque si quiero cambiar la forma de guardar la imagen no tengo que modificar la vista, solo cambiar la implementación. Eso hace que el código esté menos acoplado. La desventaja es que es un poco más compleja y tiene más estructura.
La versión sin DI es más simple y más fácil de entender al inicio, pero está más acoplada. Si quiero cambiar algo importante, tendría que modificar la vista, y eso no es tan buena práctica.

3. Qué tal si tratas de comparar estas propuestas con lo siguiente:
- La versión sin DI se parece más a la programación estructurada que aparece en la imagen, donde todo depende directamente de lo que está abajo.
La versión con DI se parece más a la programación orientada a objetos, donde hay una interfaz en el medio. Eso hace que la dependencia no vaya directamente a la implementación, sino a una abstracción. 
