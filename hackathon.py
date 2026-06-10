from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>guidetorome</title>
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
        <style>
          body {
            font-family: 'Great Vibes', cursive;
            background-image: url('data:image/jpeg;base64,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');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            display: flex;
            height: 100vh;
          }
          .sidebar {
            width: 160px;
            background-color: #333;
            color: white;
            padding: 20px;
            box-sizing: border-box;
          }
          .sidebar a {
            color: white;
            text-decoration: none;
            display: block;
            margin: 15px 0;
            font-weight: bold;
          }
          .sidebar a:hover {
            background-color: #575757;
            padding-left: 10px;
          }
          .content {
            flex-grow: 1;
            padding: 20px;
          }
          .smallSize{
            font-size: 25px;
          }
          .sidebar a {
  font-family: 'Tinos', serif;
  font-size: 22px;
}
        </style>
      </head>
      <body>
        <div class="sidebar">
          <h2 style="font-size: 40px;">Guide to Rome</h2>
          <div class="smallSize"font-family: 'Tinos', serif; font-size: 22px;">
          <a href="/">Home</a>
          <a href="/maps">Maps</a>
          <a href="/food">Cuisine</a>
          
          <a href="/quiz">Quiz</a>
          </div>
        </div>
        <div class="content">
          <h1 style="font-size: 80px;">Salve, Citizen of Rome!</h1>
          <p  style="font-size: 40px;">Step into the heart of the empire. Discover how to use a map, and learn about the food that keeps our great city thriving.</p>
        </div>
      </body>
    </html>
    '''

@app.route('/maps')
def maps():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Maps</title>
  <link href="https://fonts.googleapis.com/css2?family=Tinos&display=swap" rel="stylesheet">
          <style>
          body {
            font-family: 'Great Vibes', cursive;
            background-image: url('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTEhIVFhUXGBcXFRgXFxcVFxcXFxcXGBgVFxcYHSggGB0lHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFxAQFy0dHR0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALoBDgMBIgACEQEDEQH/xAAaAAADAQEBAQAAAAAAAAAAAAABAgMABAUH/8QALBAAAgIBAwMDBAICAwAAAAAAAAECESEDEjFBUfBhcYGRscHRBOGh8RMiMv/EABkBAAMBAQEAAAAAAAAAAAAAAAABAgMEBf/EABwRAQEBAQADAQEAAAAAAAAAAAABEQIhMUESA//aAAwDAQACEQMRAD8A+hRWSm0yj3HijyJHfoRiTnGW+LtbEpWurl/12u/bd9S60zYDBrQS6lUT0/sOxxNNZkCMUM0URvkaIKCoFEG0LiFoN0GER2D1HaugOAYegmMhKGsUAt0NFgUaA8DI9msnY6Y5Sw6ZrAjSKJHUkRstVk9RGVaRHVRG7LasGTcTOrgtL+gf8ebXnQEXgrDhhBUNl9A7MDxTXqbUiPC1yakSfUvOPT7kJLqZ1pGj1OfVWRr7C7SKqPao1BB6HSwO+MA2rqGOSiQ80k0ua4Cna49iu0CDBpIKisY2UUEwxhRc5TaGyjJZKOQKLxOklAVJotQYxF+T1BIMpUW2iuIYNSi8CKJbaK4E2HqcZtjPIXChJw9RUFnKhlL0I2USM5VOiIJMEGCSNd8J+lQk42FIaiDR2E3pnUhKzgVh6gomwdM4EmshmDUqfQ0lY8l1EUun0EaUokZQ5R1aiIZuyLFxySiTkqOvWheTn1XRnYuV6zaFvN0LNZQ0DZkeSspCWBFHHHqbTXd/scJ0JhNoxKqJrJqLWiFIDGRpElM2h2hKyFAuK5rI0WKaSAjAaAh0wDUK4hMwBZJE0ioKJsNzThRk8eMrJEnHJlZizwQ0zBWS5EppDxXI8Yk5sMwaE1gXTZSZFKiapWVEJMpuROcgtETkSSXcq6zRGVEVUGXYCQdNNq/gKQjJLTOTUjR3MjNehNipXY41lcsyQzWTKBtjPQ68BjIagxiGA2hZeyMVjBSHBpyimSGQsQxKhGMFBRWJKkBjSMGGRNmQ1GoQBM1GRmxAEM0awgCTIyR00TcCeuTlTQ6iZQKMJBaFE5RKpGkirC1FonOOTokhJEXlUrmkS1GXaJTiZWLie0lMuyE/2TVQ+lqYarn4odojpPJdBAScOxOSOlMikm+aCiV01hWaI8sgqjbENQwVAZxHha0UUSFQ7LiaFDIDChkYLFSGKhMKFihQKZmBs1EhooxohaAMY1GigAoIDIYZoyRmzIQMjUCwplETUIzaKfyDnyZdVfMLIlRVeokzKtE7JTRb1rxizgTYeoD2IjNkqX3E5oVWM3fIaMdcXkZiabx8j5888o3jM8JBkydjxZWpsPBjkrKqZUKsZI28KGRkwsCGRUTSgYwEwMqM2YO0kNFhRmgIYO0CghZRFYIgkxbJ08PZrJOQdxOnhmxkxEghASeRGh5MWRNOEonqwKMWTIqojD2F1sDahKWeSKqEg8cD7QNUNGRKqWqEkys+CNCpx16WPQqmLQ8WbxnRVdRNozCMixfnuUgKPFDhU1jJiBTKI4VIVBTGRrBZqNQyBDWFIziPA1gRkOgIthZmLYAGxZDCyRNUWSBCI7QULAJmqMZsYTbJtFGTbM6qEaDQzQaJw9c0oiqJXWRJSIvtRJxommX1H+jnV2TVQ9koyKSi+RUhG700IFBOhmEWVTJsZMIVUcQQiCEytlzykuzBooqjUPC0qGoCGYyazACmMCkMKjNjIJGTAYRnA0BAkFANi2EDRBlugqViT4GjxYjURmZNATKIskTaKSJ7jOqhYPuOySVj7qwyJTsK2upHb9fMjarIyu8EWqkPa/wRbyMqeV55gMkChi7XnjJ0WSA1Y7CiiDGWDlhq+f0Xg8FSlYonYz9xUikYlxNKikZAoKRUKqxbGUhEMVEiZmcTDJmAZsSQUGZosUzDTO2LYLNYaFEzUKmBzHpYahGOmBtCoc88Gi8B1USjaMr4q4s1Y6JBQ9I8pEtYLBLgm+TiSDuJ619BNKVKjLcrTFNSRz7irI6kCacUgsAsSGpjqZq353HKMWT5FiZNrjt1J5QxE4QeC8Jdjaf48+5SKKnItPCRbTOaOKLaUrLlRVn8GgYG4tCraRlIhdjpj0YrYqYAtgDNiSQEwbvUNApOxmjRQOoBkBSCjbQAxZpE1I24WjFUw7iUJG1Z0PRhpsmkLKVmjL6kaeNeQsSTszvgWnjbhnIEkIiTM6rBwfyYNN1m8npQS7kP5ELI/pzsVzcri0NXhO/2XkrRJxVjQ5MudnirpoafoPWPv2DeOSGrqPpx558mnpPtZ8Cx7AjPHmTTaHoMDc1l+dhHIdW16j0YZO/gtoI5oTL6ciuSrpsRyXn7MnjIheoxZUK8Ggx2MgQzQilkqmOEkBKjTkZ5JM0WaZoxoW8j+A6YwsB2hwitGjEKgEASUSWodEpE5xQrDjlcwqXUScUMo0ZS1asUM1kSAzkVpNJ9DQDYJMAE32JKNPPnlFa6gXqTfNNOemI4855OiLJakeewrBqWGsk9Vrb+ENJ8+f6I6rxZFqoCb5NqtiKXCr5NqN9ydXh4O/YdS/ruc8f2Vl086sqUY6Eiu1kocIsufOxpGdGYYvhEr/Ay8+hWkvFjt5JQGk/v+GVKmixrYImk/uALNMMVgwH5/gQO3kRvIehKDyOjF4y889x0RXUdMJSsPuGslL8DR5+ByhtRkJ6uaOhnFq/r7ojunyDkuGXo5pcstpf+X7kc1VEauwNFclP7KhEbFTBPgSHDFpqoGywR/H4LxHJpEUSUpL5NqdfOhPt7sXV+HITVX1EUVWSLfPuxnx53M14hPPHsSnqdW6BoPD87nP8Ay/1+TG1rI//Z');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            display: flex;
            height: 100vh;
          }
          .sidebar {
            width: 220px;
            background-color: #333;
            color: white;
            padding: 20px;
            box-sizing: border-box;
          }
          .sidebar a {
            color: white;
            text-decoration: none;
            display: block;
            margin: 15px 0;
            font-weight: bold;
          }
          .sidebar a:hover {
            background-color: #575757;
            padding-left: 10px;
          }
          .content {
            flex-grow: 1;
            padding: 20px;
          }
          .smallSize{
            font-size: 25px;
          }
          .sidebar a {
  font-family: 'Tinos', serif;
  font-size: 22px;
}
        </style>
</head>
<body style="display: flex; margin: 0;">
<div class="sidebar">
          <h2 style="font-size: 40px;">Guide to Rome</h2>
          <div class="smallSize style="font-family: 'Tinos', serif; font-size: 22px;">
          <a href="/">Home</a>
          <a href="/maps">Maps</a>
          <a href="/food">Cuisine</a>
          
          <a href="/quiz">Quiz</a>
          </div>
        </div>
  <img src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1566734716i/28049089.jpg" 
       style="width: 50%; height: auto; object-fit: contain; margin-left: 50px;">
  
  <div style="padding: 20px; width: 50%; font-family: 'Tinos', serif; font-size: 20px;">
    <h1>Map of Rome (27 BCE)</h1>
    <p class="diff">
      This map is designed to help you easily navigate the city and explore its key features. 
      By looking at the labelled streets, landmarks, and public buildings, you can quickly find your
      way to important places like the Forum, baths, or markets. The map also highlights infrastructure such
      as tombs, rivers, and camps, making it useful for understanding how the city functions. This map 
      is a practical tool that saves time, helps plan daily routes, and gives a better understanding
      of Rome's layout and resources.
    </p>
  </div>
</body>
</html>

'''

@app.route('/food')
def food():
    return'''
    <!DOCTYPE html>
<html lang="en">
<head>
        <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Food</title>
  <link href="https://fonts.googleapis.com/css2?family=Tinos&display=swap" rel="stylesheet">
  <style>
     {
      box-sizing: border-box;
    }
    body {
      font-family: 'Tinos', serif;
       background-image: url('data:image/jpeg;base64,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');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            display: flex;
            height: 100vh;
    }
    .sidebar {
      width: 220px;
      background-color: rgba(51, 51, 51, 0.95);
      color: white;
      padding: 20px;
      flex-shrink: 0;
    }
    .sidebar h2 {
      font-family: 'Great Vibes', cursive;
      font-size: 36px;
      margin-bottom: 40px;
    }
    .sidebar a {
      color: white;
      text-decoration: none;
      display: block;
      margin: 15px 0;
      font-weight: bold;
      font-size: 20px;
      transition: all 0.3s ease;
    }
    .sidebar a:hover {
      background-color: #575757;
      padding-left: 10px;
      border-radius: 5px;
    }
    .main-content {
      flex-grow: 1;
      padding: 20px;
      overflow-y: auto;
     background-image: url('data:image/jpeg;base64,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');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            display: flex;
            height: 100vh;
    }
    .food-section {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      margin-bottom: 40px;
    }
    .food-section img {
      width: 300px;
      height: auto;
      border-radius: 10px;
      object-fit: cover;
      flex-shrink: 0;
    }
    .food-text {
      flex: 1 1 300px; 
      max-width: 600px;
      color: #000;
    }
    .food-text h1 {
      margin: 0 0 10px 0;
    }
    .food-text h3 {
      margin: 10px 0 5px 0;
    }
    .food-text ul {
      padding-left: 20px;
      margin-top: 0;
    }
    .food-text p {
      margin-top: 10px;
      line-height: 1.5;
    }
    @media (max-width: 768px) {
      .food-section {
        flex-direction: column;
        align-items: center;
      }
      .food-section img, .food-text {
        max-width: 100%;
      }
    }
  </style>
</head>
<body>
  <div class="sidebar">
    <h2>Guide to Rome</h2>
    <a href="/">Home</a>
    <a href="/maps">Maps</a>
    <a href="/food">Cuisine</a>
    
    <a href="/quiz">Quiz</a>
  </div>

  <div class="main-content">
    <!-- Breakfast -->
    <div class="food-section">
      <img src="https://i.ytimg.com/vi/dkbwhk1Eq80/sddefault.jpg" alt="Breakfast">
      <div class="food-text">
        <h1>Breakfast</h1>
          <p>Bread,Cheese,Olives,Honey,Leftover Fruit</p>
        <h3>Nutrition</h3>
        <p>
          Protein: 12g<br>
          Carbs: 40g<br>
          Fat: 8g<br>
          Fiber: 5g<br>
          Calories: 280
        </p>
        <p>This breakfast is balanced with protein and carbs to start the day with energy. The fiber aids digestion, and the moderate fat keeps you satiated. Overall, it’s nutritious and easy to digest for ancient Romans.</p>
      </div>
    </div>

    <!-- Lunch -->
    <div class="food-section">
      <img src="https://i0.wp.com/cibiantiquorum.com/wp-content/uploads/2020/04/f9ffc-a1ebbb_93d8662f0fa745cfaca425ce76b01c85mv2.jpg?w=730" alt="Lunch">
      <div class="food-text">
        <h1>Lunch</h1>
        <p>Cold meats, Eggs, Bread, Vegetables, Fruits</p>
        <h3>Nutrition</h3>
        <p>
          Protein: 25g<br>
          Carbs: 60g<br>
          Fat: 15g<br>
          Fiber: 8g<br>
          Calories: 550
        </p>
        <p>Lunch provides more protein and carbs to sustain energy through the day. The fat content supports nutrient absorption. It’s a hearty meal suitable for ancient Roman daily labor.</p>
      </div>
    </div>

    <!-- Dinner -->
    <div class="food-section">
      <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxQTEhUTExMVFRUXGRoZGRgXFx8dIBoeHhsdGR4bHh4aHSggHR4lGxoaITEhJSkrLi4uGh8zODMtNygtLisBCgoKDg0OGxAQGy8lICItLS8tLTUtLS0tLTItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALcBEwMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAFBgMEAAIHAQj/xAA/EAACAQIEAwYDBgUCBQUAAAABAhEAAwQSITEFQVEGEyJhcYEykaEHFEKxwdEjUmLh8HLxFjNTgrIVJENzkv/EABoBAAMBAQEBAAAAAAAAAAAAAAIDBAEABQb/xAAuEQACAgICAgEDAgQHAAAAAAAAAQIRAyESMQRBURMiYRQyM3GBoQUjQlKRsfD/2gAMAwEAAhEDEQA/AF0I77yi9B8R9elT2MOqiFEVdsYN7glFJA0J/StWwrj4lI9RULi6LbRTujVT7fOpFry+uh8ta9SgaCRjiogdaYuB8MW+mIn4ktZ1/wC0yfpS9eGtCjSO4a8G9etXi0VGGp3qhfw6yTGtX7o1qC+NfWtRhCK0c1tbOgrV6I4huVC9FcYi9xZaIY5wT1AOlC2rUDdkDjShttdx50SrfhWHBvrm+HOs+kiaLlSZiVsFulVO6mT0NdB+0jgaWMbcS2AEaHUDYBhMDymaVgsVsZmThYHmtkOtFT5qp9qrXrAkELFFaBplVBV/C4Rn+FSYBJgToNSfQVWs2iWyhSxOwUEk+gGprrX2Y9nL9trr3sO6q9h0UsAJLQIgmdRWZJ0jIL5OW3UioDTFxzs5irEtdw9xF/miQPcaUuua2ErR01TI2UdB8q0NhenyqSa0ZqaLaRC1ocifnWoU8m+dSPWoNaCZmf8ApNei63NflXlYK443GKHMEe1SDFr1rVDW7IOgNcaeC6DzFTLcPWqxw69BWv3YcpHvXGFzvDWVT+7n+ZqyupHWfReGw4VQqjKo2AH7VaWz7+1b3lYKcgBbTSY9/lXmDxT5cty0yEE9CN9xB0+VXaWhRBfwiHe0resUMTs3bdiO7yaTo/L0NG8VikEEt+f7UNs3bfes9nO7FcpmQu8zLfoKRn48fQzHdhXheFwmHBC+G5ENmMtrrETrPQVX4ni8KZUokeg/z2qjZsjvZbW4SrZgdo2joBAFFLmGW4CHVWB3kV5TxxTvZTzZyrtbft4e+VQHKwzLGwmP70KwPES7BCpzHYDc+29MfbPg4W06q3js3QUk6tbcAlfODNJl3CujhkBncsDJk6n4T10inqEWjObGDEWWUw4IPQiKr3BtRTsVxT73ibeDxCG7OcFoIZIBImOWm5jcU88U7E4QCEa4G8mzfQ1q8aT6OeaKdM5UvMdDV3hOFW5cAY89B19aN4vsiELRibYP8rgqfbrVTE9ncQqjIoYdUcEk+kzFBLHJPo2UlKNJ0VOOYTNc7u0ZW3JMRCknWOtB8fhGRmGUwsT5Ttt1oimHxFlye6uLpqChiOc1DZxbC64zeBvinkD+saUHT3oQ249GqcCdmRQwIeACORPI9Imur9nfs7wlkA3VN5+ZYmJ8lBj5zXKeF4023VgZGYSJ8wa7ot87zoaDI7WhmKbd2XMbwPDXf+ZZtuYiWUExyE76Vyj7UuyVnCi3ew6lQ7FWQEkTEgidueldbwt0neud/bJxSEtWssySdfIf3pcVTCcqOW4bBs2Y5TCqSTHSvRlAmQQR1q3wbFxauDWWBHlE7UHF4qjKOcb+tPavYlz5PZ1T7F8Hay4i6VBcOqqx5LlmB01NdUt3hFcd+ynGBLGJkgQysddhljn6VexfbW9baV7uD8IPTqSD70uSuQxzSWzqN5A+hAM18odp0FvF4hE8KrduBQOQDHSu68H7b3nKqbCXCSBNtzuTpIymK4V2wn79iv8A7rn/AJGqMCSbAlKwV94brXoxR5ioDXlU0CWfvI6V6LwqrWV1GF0OOteg1Rr0Guo4KW63FC1vN1qRcYaygrCMVhqmuO6ipBjFrqOsnrKh+8L1rK44+p2BG2tD8TcPfBPwlZjzowsA6xNAsfjFGIY7lUAAHnr7VZmmoxsTBWy53IjalLF8edMQE7si3mgkDrz22/ailvF3LwaDlAEwv70GuECZ389fzqDP5cKqKKseB3sM3zDBxBI0Mcx/beoeLY2/FsWJ8R1YcunoDrr5UPs5dDMA1Hex/wDENsHwyMpPIzrUCypypj/ourRW4pwdsuIuXGZmRZAXXM2XNEnUkGB70k8Ntvdc+EhFJnTfynr5U7catXU8JuQGmBn3PoDrNULKuiG2UII2B0g+s86obUVsWk30Xey7LZ726XVCAAXbTQidT9ParlvtjaMlTmAJGYmFkCTqdSY5Ck/jfDmZbSkhZeJOx0MaA9aFY+w1q0ttmhZIEQYJ0zCNd/OnY8r46MeJXbGV/tFxJZgbVvIvLKDMzlkmg+K7Ws8sRaUdAgBB9RQfiN1VYBVIAgMxmSP5mI232rRnt5QEVXBMt+xJ3rXOT7YajH0kFsbxi+hyvduqGAYCQRB2j5VFw9LWjm4pE5WHPXnEjWaBcSxOdj5QBJJ0Gw1qPDIS4UnKDEzrp1pbhYLUW9oecXwBCQyXAPDoB16kHUfWuuYbW1bPVF/IVxDhXFwjASbgtxGbWRzB8o/IV23gOJFzD2nHMfkSP0pOVLjaB48ZAVe2QD3FVRCZgsz/ABGECB0hvp0pQ+0ni5vCFtNH4XMannliflTH2t7MWraXcULrovxsiqCS3LK26yesiuZ4zjL909tjpErOuUgyPnJBpS21QMpVoqcLxbWwUe1mtnzgqeoJGvpVHFlfwnnsdD5eU1Cb5cKees+VaFAdCQPOqq+RATsZlw8jMAzwwnRo5Ec66hwfgGFZe/vHOIzEudAImIHTauYcNTw5S0pmmNjMbweRj6UyrjLmItlLcbfCCCT8th/akZU21Qa0rZ0K3244fhLcW4USYS2up5TA2kjcxtXFOM30u3rtzLAuOz67jMSeWlTY/AXRvayx0G/rJ3rTAYhCCr2c9ydPEdR0gdOtHFVtA8mwO2GHStGwYpxwnZ17rSy5BGyD668vTWj1rsSgUHKzHfXp6VkvLhEsj48n3o5Y2B86jbBnrXZMN2Zw9tszWUaTswmPrpRu3Zw6aDDoum4trHzFZHz4M6XjNHz13R6E+lFOG8Da6juZWB4NB4j01MgeddrxvFLSI0IoaDHhG8acutcov8XYttEb1THLyWhX00nsV79hkbKwKkcjWkV2rsucLiLTG7atsFj40DewkTW+O7M8OfbDx5pKx8v2oH5cI/u0b9CT6OI1ldT4j9mlhhmsX3SZIDqGHzEGlPF9h8UuqpnXqu8dcp1pkfIxv2A8M16FiKyrjcPcaEVlNtAUz6yZQJ5mknGY7LfvSJEx8gKfCs1zfj4i7c/1Gh/xKTWJV8jPDinKmFOA8WtTdEMM1tht8qWMXiRqNetQ4HFZHmq2OvyRHIR8if0rw5ZpSjR6sMKUic4w5cs6VWuX+fMVAjEyB0J+VQNcpLtvZSoJIZhdF0d5ILQN/KpMcwYf1E6n02+h+lLWCxbJIAknUD0q6ONoFZmBDKpOXrBjQ/WtePNJa2mRyjGMgZ20xRTukBObVp6aQN/elrvmVCSQxJBn9KMYrCfeiXW6pnXIeXvyoVieB30Ii2SB0IP616vjJQgoN7J8ilfJI3w91su6+ImZPnzHvpVfFp3TBdDCg+HbnyrdOH3Z8VhoJnTl/erS4O6Hk2wEIAlyJ+ppvJGcW6BvdFiSQdRMD6GtbryEVBLDfqfWj+H4Wyuc+m0RBA8vOjHCez1zKzLZGsQ2mvnrFZ9TejOHyB+EYEDLaEG45Enp/YV1zhPEUshLOyR4T58/mdaShwDGWznTCZmGkDICev4ppjwvBbzIC9vUkQCYy+ZG8DWlydwfywZK5Kuh275GQhoKkQQdQa5N2q7MpbXF3AAZBNpR+GRJ06zoKar/AAjE2wcp7wcgJH/kBSxxO8+tu5mAMjxaGf2pCTTQLx3sSLdpU8LWobSdfKdq9xmHVbXeaKSYVRuY3PlRDE8JuTmBDCNidaovgGZyHECOvn5VWmnImcZLspYC2x8Ww159QRTT2TsYWwxfEYgLcKkIAD4Z/ESND+VCQQpIkeeoPvt5UK49cGYZekE/5v61ji5OgmlQ8X+8vlicUioBumpb2nepOzHBUTK5ANw65jy8hFKnZTBFV7zm8hT0G31rq3BsOqiIk761F5U3H7EyvxsSS5F2zhCoAI1GwgfWrucKNdT+Ves2nSoS4nxaf5tUcp8FoelyJzZB5TPkN6ktlCMrLl6dKs4MAjyra/bHKCCQdflWrrkDe6AXFuDWyCzDTn6ddKUuKdk8J8XiLHYBon18qdu0F0pYukDTIxA9BSdwW73njbXan48rjGom8OT2WuF4TIoW2iKPT60bsWoMmCNjAitrBUbDyqtjeJC3mA1PPTnypTvts1b0kXVtoB4YKg8+RrTEWHMlcpPmdfaapm4ba21aczS22gkaTU+DxpYSV23I/autas3i/Wym9kEy2GQtzJQGfpWUxIVjePWsptP/AHAWvgKYnFhJ/EfpSJ2hM3CTudacBbVV7y5sOXWlDtDihcbNAXSNNoG3vXuearxuyLxnUxZu2elaW+H3XXMiEr/Ny+u9FsJw8uveNGQHbm0b+3nRPGccHdnIuXwwARAHlpXz01XR6U/J46iJ13A3VTvMhyfzcuh86oE0z4Xjf8Purgg5SN50ND24IzBriaqJ0J8RA0/KiS+dBY/JvU9FXg0C/aLarm1HkdDRztB2fthe8tGULQytuA0jT/uIrzsxwVmDXG/CCQOem5PQD6mKCdvTYF5hbUtcBGcyYXmQBMT6V6OCDWPZL5WT77XoXsbw822kBgDswP7V7da6sfxmIOogz8+lTYC3bYiQSJErJ2pmbsZcuWhiLVkqhYqLa5idIM+PWDP0rZOhMXJ3QqYVMTecW7d1sx68hzM9BTvhuy9qyqm87XLjbFjJP+ldlA6mqXA+GXcP3jXLTW2aAAwI09dt6zinEWuXZbwwABrpQ8rdDIRbVtjdgeG2LFlTbUM7sQWbxEbnSdByjSrHD8QJulmJ7pQTOu5jn03pQw2KuBlBgoSM2Y6b76TtvNMAwz2rxDsO4vqVkfzctfn9KK9Og3EZgWsqttjmc6sw0mT84A0qXC3mbqFBgkbk9F8/PlQPGcRK2VfP4hC3YGwBhiP+3Wi2LGREt2RuFVZ38XiLE/Mn0rU9ANF+1dmfGQAY5n2B5mgfaTs3bxY/iC4WX4SjBSJ66EH0NEsXeyKMoM/CgG56D3OteXWFu2EcliYzAH43OsenlXMyhIxHYrE5cq3bYGWPGpLHlrkkUN/4OxZUqzWyQBBt/lDqI+ZrpOLvuvhUHSJy6KD0nc1cwt0wMxjkRGn51ij8Gu2tnAOI9mL1oE/Ec0FROaZ6Hfz8qHP2exLKWKQF3k137j/BlvQVZFuDZugMSCDyMUqcUw1+yCXtSDKgoZTXnpqPeseScECsMZP4AfCsERh7YjZRTTwXEzAMBojWlvsLiGYNhrnx2zp6U2Nwknaos8LkPg6VF4X/ABcq8EOxDLp+dBMaMRaU6ZlHXSPeoLfFrqxnsssgEEkAEHY77VLLFNjY/gecMQK2u3YOvLX2pbwfF2a5aQrAZHuZhrovT3I12rbD8YXEXO7yvb3kyCI3mOlHHHOgKu38FLtrxoLaZB4mcEKPXQk+1LHZ6/4MuzqIPmORprxmFsNpmVm9ZNJ3aDht22/8NEaNZS6CR8vyp0MX28X38nXQ0nFeHTfaqtsnWfn70o4bjlxPDdBA5EcvWmXAXz4WGqt8z6fnrQTxTQcckYoPcWeWy6aKPXWswODE/E0RA/z0offxT5jI1VI+v6VfsPMR0G9A7BUtaCltIAE1lQtHQfOsrDLLHHsSzmF2/Kh/E+FK9tdQGEHXUkc9BUvF8ctlC7b8h1/uelCU4k9oMb58TagLJygfhJ6z/mle/wCV5ChF2rZ5sIvtFnEXLdrIicjATc6zqRz11quuAS+zlmZcoC5RpmJ5yeQH51Z4ncTIGGXNKgMBJ6Zp9K8bGWkvqQJ3Ean0nrrXgN1sZYm8V4Jlv92jiTr4t5PLTkau4U3MKndXiCGEKeRHMbAzrRvGth7uJtZtHU5piMwH4T61L21vW2sQSuZnULrznUjnoJonlvjF+zUUMWbVvDOyCGVfCVOpPmeevKlTA8HTEOWN1w7kkjTVjqZ0pns8Mt2k73POUSVMAeZA60N4zxC29tmtwHUSXXlpptVGDLTpb2Fp6HbsR2Lw1oLey5nPwljMAaaeZ60+iAIER0rl32V8ZLYFVmTbZl+uYfQ03X+KsFJAkgEx18qfkg3J7MTTVE3aHieHtgpcGbMPhAG3UztXIeIWFYsywyA68yo6xz5TFX+L8a+852yMrEgNB06SCdQdNQap4LhqLZdQ7Wg2rNOZtPNht5CK6MVFFMY0DLmFIUhLptsykEDUQSJ0NS8N4pdSz9373vEhoDpMe4MiDVLE8Pe03eNcNwONCBrA6jkaG4riRCwgg88w1pkYv5BlKvQ04bjXdW8pEkRJDEnffamngfaJLr2nuXUm0+0gEgiBI56nlSPwy4uSS2U7lv8AesNlGvrcVPhg59FzMNQYH+Gg7ejZOo7Z084gvxC2CxAQMQP5tIHruanw+LJxLaTCFh0BmPr+9c2tYu4t5CbrlM0kkglBM6E8idKaez+PzG6S8u8R5hZM/Xbyor+QUk+hqS+F1J9qiu8Q3gT+Va47A92EME5kVvnyqAAFabyCUbPdTqOdVsbYussKfhIPkfI1LhZJ3AUzqdJjp78/OoMbdzc4A1LE+VBOaS2Eo0wDxBQl23iV8NweCeTAa5T8zBppwPF0uCVOvTpSreP3ohLa6JJJ9dBQPD467YuwAZB18/2oVic8aYpzSnTOhcRuXCCANCIpRw1u61v7m6lraMDbb8QX/pHqvMdAKO8J7QW74y5grRsd/wC9SjCX8+axiFtmZ0UN5cweVITcdMavkscPuXDYV2RpskrAgZrbnIyCdvwsPNRQC5g71m8L1tQ26kMwGZGEFTG2nTmBvTRbwV4j+Lfe4d9YA9lUACqOO4ZcO2ta3vR19+rFnjWPU5VW0UjUqWDSZ6jkANvOh9i9bJPhKvyI9edFuJcGubqpn0oXhuAXmuRbRln4i4gUyMjHvsJ4/HWGw5L25vBSCY0zDn+tKh42WMz5D0p3v9jHy+FwWjWedLN/7PcVm8ISP9VHDhexUr9BDgrfe7qWy7LMyVMEQpP5054TsvbTe7db1c/pVTsh2XGFBLMHukQYOijoPXqaLcb4h93tNcIkiAB1J0H70rJxb+3o1NpWyZeF2QIyj6/vWVzJu1F+dbrz5GsoeP4EfqEMnaFlu422l2QqktvEldAv66VV4/hBeaFO2+tMHbPs/n1nfUHo3Pzrn+GuXsNcZShcMNTMx0M7RTfJxTc20+jF1Y49k0W1YMg5szAk9BsFJ5enWgtjjCLcvFFbL/SCdtT1jWreG7TWxbVGBkDbkSd9RvQe5xBFDKFIzEsTMa/KpVhnJ2zk9WHsZh8Pesd6cpfJOfY+3SK3xGPwrYbKwXKFXLO8jbXfNNJnE8GXAa07gaFgokTylRzqC9gbtxQtxltLMkn4m9uXvWfp5OrZ0XYy9oba3sNltT3hI8K/iEiQfLn7Ur8dYYbCnDr8b/GevX6Vvje0CYW2beHksRGdjLH9h5ChHCePIc33kZjqQ0STJ+H9qqw4JQj8hSmkq9lz7Pe0P3e6yt8D7joRsa6wvEFdZBrjZv2r10CzbKgalzv6R09absFxN7aQVWAN58qbOLe6Aizfi+NtWwRGs7dT19KG8H41musLhGTLty3Gkc6C4m495zcaYJ09Og9K0fCNyU6nc6A/OJoKD+pKUrXSG/j2EzWO9teA2gSAOY5+9LtjHq65r4WP5joT6RvUmE4Ri8pVSEBEEF9CPQV4ezF873LcnTY1ilDptFEo5X1E9Q2mUMi5Lak7ncj8R6+9a3cdl0CnL1ArVOz1+2QS9th0kj5SKn+63UEvaMfzKcw+lb9SPp2InhyXbTK+Dxb3rtuzbOtx1Uc9zEk+Uk13Xsx2Zs4dRpmfm7bk/oPIVxLhGVcTYuoQCl1CeWmYTvsa79g8WDFBOn0dDSCyWusEchGw6VQ4twtHtsQAGgkEenON614hxu1h0D3WhSwWehPXyogt5bluVIZWXQgyCCK1MG3FnH73GLdseFZj2pcxvFbmIfLnVUBgkmFHy39BJofxXD3FdlZgSJ8K/rrPtWdnwVxWHW6gAJY6gHNoSD5QYGhjSuji47ZVLJfR0vghs4W0ot22dm1LP4cx6wASB0BigPFLd3EXS9vDrIMEoxPzkCjGKu5VOXUxqee01LgCLeGVUMM0lm6sdd/Sk/rMjX4+KN+jFb9iPxbg9xdbto2/6hPznaswXEcRY1F0XABs41+Y1+dNaY9TeTDs4lyfiIM8yOhnYCveOcEshwi2ykkBSpMGfMkiu+s2vvQaSTKuC7dlSBftFZjVSHGokA5dRprTHhu1+Ef/AOVR5EwfrQx+y+Hw6ENmuMdSToBy5bA+ZoR2q4VaS2t0AhSIyrACnkSWOg61ynBy4oGtWdAw+OtXPhYH0M17edOZFcZVEAkW4M7hiNOnrtrNe4a6paGvXra9czMB66zTo4rdWBJtK6OuPjLY51UxnE7eRhm1II3j6jUUu4Lsi1xQ6YjvUOzKxYH5Gr2L4CMMELgEMSDJ123A509+K4q5S0TvP+AFj+IPbDNbJ+JSCPU76Qff6V7xDiF3EW5IRgokhtAPP1q1juOYRc1u5ausm2ZSAQeRA/c0sW8UpQqWA12InnpMbUmUIwkmnaEPI30BLll5P6CvasnFv/I3sP7VlFUvwBbHvtTx1b1xbaXCsHUzAJ6DmdAdaVMaSAbUAc5HXrXnE8Oty73dlCx5BROs61asdlsTlf7w3dZBAzalp2AIJB8/PSmOTnK7/oHTi2DeE+O7DNOUAjLz1g/KtHxoa85G231q/huyWIS4HtmFBKu/xDWDqoM6TB6RVvi3YgW0LnFKC0tATWCOSlgQZ018qV9SHLTCjCS3RtbtizhDiCzB3jKu0CYnzJG1Ub/Cy7AhXTNtmEz6HaqmN4qbtxLWmVSqsNR8IB1n0p24bxaLcd213KoICeJoI00/zanR/crMtnL+O9m7tol2By9f96BphiTOkU9ca7u4738U2IY65LPdsqIBss/mRFAeC8HuYtyFAS2PiYDRfIDmfL507JJRV+jYxlJ0uytwEReAA8JBkjYRrPpTL3veSsShEef+1bcewa4bDlbYjMQCeZ56nntUXBbmZVPOD9P96neTnByQzNjeKSj7C190tWu9cA5ZCjT2A96XuFlr94PcJJ3Hl5DoK34/jluMttDKWxqRsW5/KvOC2b7tkw6F23hRJ9SeXrSYwai37Ycsi+2D6VX/ADHpDGlQYnVSJHkRyPKldsbdtv3d4NbeJB6/PSKkbiFwDRgfJh+oqX6LRdLzMfTsI4nE50OwYb+RFR8Mx2YETQHiuKLISoKk6MP88qp8JxDoZALARI9acsFwYP6tKaXr5G3F4O3cAzKCw1B5gjUa04cA7SiAtzcaZv3pCTiAcc1boa2wmL131/z50EVNaHTjjmr/ALnWuMYNMZh3tZgMwBVt4Yag+Y/ek3sf2nuYC+2ExJPdSV1/A3IifwN+tSdnuOnVdJUx9KW/tH4uty4lsKDcH4hoQOlOhFt7PKyKtoGcReWZobPnYmdviJGx6RvTZheDWciFbSFmUMzkScx3CknwgUm3cUbgDQJIGb1G+vTn70Z7Mcdaye5uibbHwt/If2ocyk46ZZjrvsK3uE3nuFbJyuQSAW0005nz5VJhsVibNg2r9gubY/AwJMGRMa7GI8hRbhOPQ4lLgZWBR1EaSd49dDWYWybt1MzQSXe4AemwB9xPkKmT1TCe2UMbgLdxbbsoLtBLAayBpB306V7jONmwyW74kSGS62o0MwejefPnTJewimGUCBqQYkab67HzoNiVt4hrtt1zIoBytuT+2tBy3b6N7VIN8dQFRcBzIxBGvXQD01obxJFFpluKrKZUAiZ3G3TTahHEr62rJtopRJGWNhBkaHloKL35yLAUl/FrBgnWBI5E71v+m18mJbpi9iOH4R1yW4tPEBVGkx/LMcvKle6IZkIh0+JeccmH8ykazT7ftgFSwQsusEAGfJhrNJH2g4R7Vy1irZ0By5gNQd8rdRuJ5zFV+NJyfFi8r47RnBOP3sJdD2GK/wAyEHK/kf33FNnHu05x4W/bS4q2kAcDUW3O8nodIPOkJbwYB+TCYnbqPY6VtZvshlSQjwrQdG10mD1Gk1XK3FxZLlgmrLl92JJJzT855VLdy5MvdywggbSToBINRYiV30oe+IfNIYjloamqyNMODiF1PCZGXSAxgRWUAFxv+o//AOjWUzj+RvJfB0DsBhg9lUYRdLE5svxD318IB05mjAXPjLi3VdUS14FLEAyYnMTG0jepntW0vTZUA6wZO8a69OVQXMRYu4kd9cgskKpLDvIMgoV6Ea89amhm5TcY9P30WOFRTBPFeJ3bAZApW3IBA1idJLDw9Sau8e4TbTDNfFxn0z+Ejbc5Rt086J4rhFz4LbXMh8WmuUEaqZYsd51BmqmMwbPh7lvDkG4ogKAEKyNCRMEEdIOtc7lSxNUn6YK1tiD3jY1mu90ltEV2zTroIOc6bxt1o12cttaw1245IzusHyCgClIX76K1h0ZS2jq2gMa6nnvymZo/2jxnc4WzhgxzZZuHnPT11PpV8Y8aoRt22DcTiu+a5mgp8I6kjc/3ozwe8i2mRPCqodt5A39+tKGHRioZQBI0HkNNOta2Me9tzGsggg+Yik5oubexuHL9KX8wriOJnEYUrdWHTIQwHxiQPZtfetcJgAq/xGKjWFBgwep9hpXvD8cgtMxEnJK84PMken1imh2wIC2LtwpdYLcUsQggyCHZlIJjXJ51uRfT+2PT2MxzU/un2tFThPYqxfw9y8t8qUMEaEL6g/OoODYLF8PnFW2Fyw5NtzG3iCkkGDyIDHTWq/GOE3bIS5hWCqzhWbvFyyDKMzZoAOYiCIEEc6Y7i8Qs4O/bz4fEC5Lls5bLOjaEAEaSAPlS7dLen8nVFy0iH7RsXavLbt2UR7zEMAhUuoJiMwkQTplkbTyoHj+yT28NbfI7Yhs2eyLyrlUAsG1EGBlkSd6d+ylnCJYKtftm5MOBC5JUAhSANdS0jmTSF9ouJsvcz2bmdEyKoFwFWDLBcAAEPM5hERWY/wB3FHS6LXFuyQw9oXM6vbOUDMCHlhmjTSYnoKXsMnduZPhiJj3FR8JxWIxLJh1ZmAOYKzEgZRIgEwOnvTpxPsxct2gXa3mjxqGByk8t9efyopXDUnYVRnH/AKFvFWJGdTr5c/71X4djAGZiOX15V7ibV3C3DauDSAeujCQw9QaHYsxcJGza/SKZjJblFOLD3C8YqBmYn+II05cjrNBMZYdcrF84OockkwORLazV1eGs2GFwTIJMdV2/vVXB44FWtPqraf6T1FYv3No2fOKSl16/qRYa8R5n8/70U4fjAw8J1HLmKGYrBvaK51IDDMh5MJIkH2qyOEF17631M5eR/wA1961qPsLBkknSDbQYk6ggggwQeoPI1dHaW9mUKme6pzSu5GxDDbUUsYfH3rbA5S5XUEDUcttjRWzxCde7ZCZDDumWZ3k8zpvPKgeJPsq+pfR0js72itYofwyodYzWyAGXyjmJ5jSouOZUu2rjA21Y5WaNJ5Bt4BOk6UkXcXZIX+GkJsQArMeZzRPltpFW8ZjcRczg3ptO2Xu1fMIjcAkkLpv50iXjL09Gxk7G/H4AOrTGSCNSNJ/XpXnCcaty2AHBe0CpXTUcj8hSThLt2wMi3GKj8LMWA8hJkfOqCYMi93y3HRidchgUC8f1YTs6RjbCXFn4ehmDt1pM7V3w1i7aWWJEADWCNQan+9NcADtMVWeyoOUNBPTQ+8U3Hi4bfoXO2mU+BcBYKFuMVT+kjX101ofxXBG1cNnOShIYem4mOmvyonjr3dEKr3NAZJaFnptvrEVBisQXlid9AVUeLSDJIkxTI5Jt8n0yJN9siuYO64nKxCjUxoPU7CrP/DOIlQ1ogtETtrrqRMaUZ4JgLz2AqXVyMfFnOXKV1E5gN9NpG1N93jXd2Jdrb3wICo0ieUkaDzp8MUX+7QniJGJU2mNsWxCeHROmh+tZU1/HOGIymZ1J0JPM+51rypXV9Dqx/I04K+rhGVQgeSoXUL4dJB15isuGwQq3WKvOuVYBaPlzqphsKMRjLiB2TJLE8mVgBlAHPaTVrAcNxFu4bTi3ew5ABd/CwnUDbWI+tTyhBZJKcivk+KovWMTdw121adGZbzBFYxCwCSsTMwCQfKveJ4ZP/cXHVSQrxyI0/YAzQ7F3msXu+D95ZtnxAtndBGsACefyNJ3avj13El0svCHQ6EE6ajXy/OlLx5Oar/kyWRJWAeyGBa/f766zMtsltTOZhsAPLQk152txRD3FdYdoykbBeQHTSoONYv7ubVuw5DLBJHU70F43fd7pZ2LMTzr2eLlJX0SP4D+FMIiXBAgZHHLyNaYlFcskgXF0nz5eoopgADZUMJEChHF+DEHPbNTKnL4PRzYHKCcdg5L74dwTIhgwjyO4rsPZXjljGWWF3P3kHMiLOh/EsmIjl61x92ulcjgkeev9xW+Avm02hMEEexEEU3JjU0uXaI05QJu1fCrOGxjWsPc7y2IMTJBicpy6GNDz+lF+Cdt2tTavst21l0A1IgCACYER8qeOH8cwNixaWzatjNcU5QQGBP8ADzmTJAAM7xqTtVTjHHrSC5dOEXEW0OXvbbWzBAHxSJkEiDBBigeTmlGUbDSraYg8R4il29aU+K3byLnuKobLOzZNwAeUHSuocU4BwtJU27IBBJhlWCNozN5+1IvYu/grN0u63LtySQ3gjKJIOVo1KxInl7V0DH8bwF0EtlAca97bIIkRGo0MfWhzuqSugov5FLH8IwowjXsE5t4hbphWYFsoBEDIcuU6GdazifYviN/O7X7d17OVXU+EAlVc5WAy6AjU85ocLuFtYkjDs6mSsGCvIgq4PvBn2ofi+0OIsYkvaxF0vr3mcDLLMWKxsVJIIJG5NHBNvX90A5boHY/7zYuhL6uCAAAxkZf6TMFfSpLOHF66oGg/F6c/eiPE+093G5Vui0ApJGVII0A3JOmm3nVrsrw4s5ZeegrpScVctMoxQ567RLxXh5KDU5AIABiP3pfbgRIzW21OwMyfSnntPfKqmAw/iv3YLn+RRzPQn8gaI4Hh1vB2wznPcjVjy8lHKgx5qjdd9fn8gZvGvLp6/wDaKnC+DtewK2MXZCFNLbh/Eo0MxESdQeRAXmK2w+HwuEUgH4iM2YyT7f2ot9xvYgSzBFiQqmSeknl6CiXB+F2dLT4ZkuN+Mrv11OgpWTI5fuYUVCH7UQcGwaXssErn+FVUAx18hV/FdnAM3cXybg/BcIj5gSvrRbFYa6rWVs5UCblgNugipCCLrXCJJWCIiY5j51Nu79BPK/Rzy9dv5wHsSokMJUmfeheNFmTCXrTayUWIA1J1BSK6wuHtE53QCV2O/wBfKq7vbBW2EfKx5IYHntpTozigfqSfZwzG/eAQbVxL0zAKw30MH2NR4Xidw6PbQEaGc4I9s36V0XtF2Kto+bDuynRoPLnVXCFWf+Kii6NCY38wf1qmM4ur6+Tu19r38CAnF2zZSqLqRJLcvepeJY1YUoQSNzEgn31HtTdxvA2FVrhRWO4kDelzBIhhQp8WkQOZ3M8hT5JKqIpTm3TKdvLmL31e4XAmG0kbnbXUTpFE7t4DS22gEk7Hr7wKttwvKIB02irHB+CXHuhcoC6GfpMfOlSjJvoXKTWgZw7FBbhZlN5IgrJAk7H6+9WL1/MwJGSNlAgLyium2ezaJGVR6RpVTiXZRDZuqiENcIMgzBBnSdtzpVT8Z1QNsQrqtdJuPclm3JGvTlWUcXs4yiMrGK8qd4MvwDQQ7M8SQXcgDhruZgTB0AjTpsKL47jKqhk92TObORIjaR5+VLPcNhXstmNxbKFGnT4tZ846DyoJxfEpfvG8gjMNdef6V5n0llnZ6Ep8IkHGeIrdvk20AlT4h+PbU/l6UIwGLysyOpDTy1nyq9g7RN0lVJMchOlW8Vgc4IjXcaajnV+PHVRoilLk9iDxVgbrkTvz/Kj/AAvgD4g99plhd+sa0X7J9hXvMLl+QszB3PrT/e4eLYyIPYV6KhoIRsFhMoNs6xt51FiLRUESIpm+6MryySAen61JxPsslxc6KBOsTHyqTL47vlE9DH5LUeLOZY4ENI1FVnWfWnZeyoJI7wqeUqKo8T7OXbY0YHzAn6cqFZYp8RWTDkl91C190czlaCdCDzqD7k6qULHKTJUExPWNpora4e/4hPtXowBO4Pzij5+rOxwtdAacpBGsRTFiuIWmT4h6ayPaqdzg8Dc+m9SW+CMzQEb5E/WKyThLbfQvJindUUcEqSStueYJO3+daLJw3NLv5e8ba70WwHZ140WPWiZwtmxHf3BPJZ1PkF3NTTzb+09DFg4w+8XOD8AN24cqyhBEmRrG49Drr0pj4zxmzw20LVqHxBEAb5f6m9+XOqnGe05W2VsA212zR4vbpSVwi2b+KXNrLSfQbVqg8n3T6XoUs0YVDFtv2dF7HcHupabEvbe5dunMzgT7Vf4bYu3sQl26hW0reFWBk/1R67TRPgPGBhpR/wDkuYkboTpPoefSjdnHZ8wDKzZsqkfmT0pDm3v5OyXH7SXGYtE1VJO+gjX5VomMCjxMZ3zE7c6oJw3E/eC63wwQaqwAE+UDT3rbtPgnv21FvKGZgtxZ2n8XmNKnf8wKQxjGK1tCT8WqsDUiyxzKBECZP5RQnG8LDKneQAoGqnLr6VeTFC0qgf8ALiDJ1HnPOuumZWtGmGc98xYTbA/EvPeQeYio8NxJhfZA2ayVzLlEnU+W0fqK2XEDMSFdgTuI0HvVVuGKlwvbuMrtBKwD/tRb9HUvZvxA945t59QAwLD4uUHzHlS1xvgLOjEEi6mogbx0POmy0/es4ZYNuF8zImaoYwsgW2GhdSC2pE7607HPYL0c/NsYm1DaXEke/MH1oJZbK6woJB28/L3po4jbt28Z/CJKsstPUaUE4x2dxRvm7YEqTmH9JjXT1qqEW3SF51aUxq4Vw9bq+Fsrr8SncHr6U4cE4WVIZ2zMBAMcq5jgMJiLLpdusUuqpbeS6kgEEbQDr711fgXFbV1fAwJWMwiD6wdYNXYpepdkskF3UAVWbnUjtNV7p5VTFGEJisqQWayjMo4FxPtBeZGVypESxy6xVngGBGRS/jJ+Fdp6E1lZXl4scV0hqk5djHimGDRHjM7sAxGmkHQdBUuA4gt24qEFcxiZn2rKyqHJxnS6Ftjxg8HlUKNo1NT/APp67msrKpaNRVxFpUPrVdEB02BMxWVlA1QaKy8NXUH3nXnWmI4Ta28U9Z/SsrKVKEZdodDJNdMr/wDoHhLKy+61Vbh5A/D/AJ7VlZS34eJ7obHzMvVlm1wwx+Haf80qzb4TP4h8qysrl4WHujJeZl+SvxqymHsXbzy2RSQPPlt51xzg4NzEF3MtDH3/AMNZWUM4xhF8VRNPJKT+5hXEYE3riWlgTufzql2TsZMYUbdQw+RFeVlKr/KYeD+Ih04yx7vTkwPtNHOA4Ui138Anca7QY9KysqRJODLc7+5DLhrK3QrRLMASdRy8qD4nCXrGLzJc8BABza9THXTrWVlSSATdjPiEF2wQxksunlOxqp9xD2+7DEQdCdaysrH2Z6PeG8SGc2TrlABgc9quYq5lV2GhGoPlGlZWVsDZIH8KwbHLfLlhcEOp5xtB5dK143ZGUsFg+ZJ/WKysp+JASYgP4sQfLKP1p1wWFmzIMGTWVleh4/8AF/oZl/hgu5wkScQxJKDqdpEijeK4th7JfIB3qCIykbwYkCKysqmb4W0RhDg3Fu/WYhgdRV9BrWVlOwScsabMl2Thq8rKymgn/9k=" alt="Dinner">
      <div class="food-text">
        <h1>Dinner</h1>
        <p>Stew/Soup, Puls(a porridge made from grains like barley), Vegetables, Bread, Fruit Dessert, Wine</p>
        <h3>Nutrition</h3>
        <p>
          Protein: 20g<br>
          Carbs: 50g<br>
          Fat: 12g<br>
          Fiber: 7g<br>
          Calories: 480
        </p>
        <p>Dinner is lighter than lunch but still provides essential nutrients. The combination of protein, carbs, and fiber helps digestion overnight and provides a balanced end to the day.</p>
      </div>
    </div>
  </div>
  </div>
</body>
</html>

'''

@app.route('/quiz')
def quiz():
    return'''
  <!DOCTYPE html>
<html lang="en">
<head>
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Tinos&display=swap" rel="stylesheet">

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cuisine</title>

  <style>
    body {
      font-family: 'Great Vibes', cursive;
      background-image: url('data:image/jpeg;base64,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');
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      margin: 0;
      display: flex;
      height: 100vh;
    }
    .sidebar {
      width: 220px;
      background-color: #333;
      color: white;
      padding: 20px;
      box-sizing: border-box;
    }
    .sidebar a {
      color: white;
      text-decoration: none;
      display: block;
      margin: 15px 0;
      font-weight: bold;
    }
    .sidebar a:hover {
      background-color: #575757;
      padding-left: 10px;
    }
    .content {
      flex-grow: 1;
      padding: 20px;
      overflow-y: auto;
    }
    .smallSize{
      font-size: 25px;
    }
    .sidebar a {
  font-family: 'Tinos', serif;
  font-size: 22px;
}
    
    r elements) */
    .quiz-container {
      background: rgba(255,255,255,0.95);
      padding: 20px 30px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      max-width: 500px;
      margin: 0 auto;
      text-align: center;
      font-family: 'Tinos', serif; /* quiz font */
    }
    .quiz-container h1 {
      font-family: 'Tinos', bold;
      margin-bottom: 20px;
    }

.quiz-container #question {
      font-family: 'Tinos', serif;
      font-size: 22px;  /* slightly bigger, but smaller than Rome Quiz title */
    }
    
    .quiz-container .options button {
      display: block;
      margin: 10px auto;
      padding: 10px;
      width: 100%;
      border: none;
      border-radius: 5px;
      background: #333;
      color: white;
      font-size: 16px;
      cursor: pointer;
      transition: 0.3s;
    }
    .quiz-container .options button:hover {
      background: #555;
    }
    .quiz-container .feedback {
      margin: 15px 0;
      font-weight: bold;
      font-family: 'Tinos', serif;
      font-size: 20px;
    }
  </style>
</head>
<body>
  <div class="sidebar">
    <h2 style="font-size: 40px;">Guide to Rome</h2>
    <div class="smallSize"font-family: 'Tinos', serif; font-size: 22px;>
      <a href="/">Home</a>
      <a href="/maps">Maps</a>
      <a href="/food">Cuisine</a>
      
      <a href="/quiz">Quiz</a>
    </div>
  </div>

  <div class="content">
    <!-- Quiz Container -->
    <div class="quiz-container">
      <h1>Rome Quiz</h1>
      <div id="quiz">
        <p id="question"></p>
        <div class="options" id="options"></div>
        <p class="feedback" id="feedback"></p>
      </div>
      <div id="result" style="display:none;">
        <h2 style="font-family: Tinos, bold;">Your Score</h2>
        <p id="score" style="font-size: 26px; font-weight: bold; font-family: 'Tinos', serif;"></p>
      </div>
    </div>
  </div>

  <script>
    const questions = [
      {question:"Who was the emperor of Rome?", options:["Julius Caesar","Augustus","Nero","Marcus Aurelius"], answer:"Augustus"},
      {question:"What structure was used for gladiator games?", options:["Colosseum","Pantheon","Circus Maximus","Forum"], answer:"Colosseum"},
      {question:"What language did Romans speak?", options:["Greek","Latin","Italian","French"], answer:"Latin"},
      {question:"What river flows through Rome?", options:["Danube","Nile","Tiber","Seine"], answer:"Tiber"},
      {question:"Which Roman goddess was equivalent to the Greek Athena?", options:["Venus","Minerva","Diana","Juno"], answer:"Minerva"}
    ];

    let currentQuestion = 0;
    let score = 0;

    const questionEl = document.getElementById("question");
    const optionsEl = document.getElementById("options");
    const feedbackEl = document.getElementById("feedback");
    const resultEl = document.getElementById("result");
    const scoreEl = document.getElementById("score");

    function loadQuestion() {
      feedbackEl.textContent = "";
      const q = questions[currentQuestion];
      questionEl.textContent = q.question;
      optionsEl.innerHTML = "";
      q.options.forEach(opt => {
        const btn = document.createElement("button");
        btn.textContent = opt;
        btn.onclick = () => checkAnswer(opt);
        optionsEl.appendChild(btn);
      });
    }

    function checkAnswer(selected) {
      const q = questions[currentQuestion];
      if(selected === q.answer){
        feedbackEl.textContent = "✅ Correct!";
        score++;
      } else {
        feedbackEl.textContent = `❌ Incorrect. The correct answer is ${q.answer}.`;
      }
      setTimeout(nextQuestion, 1500);
    }

    function nextQuestion() {
      currentQuestion++;
      if(currentQuestion < questions.length){
        loadQuestion();
      } else {
        showResult();
      }
    }

    function showResult() {
      document.getElementById("quiz").style.display = "none";
      resultEl.style.display = "block";
      const percent = Math.round((score / questions.length) * 100);
      scoreEl.textContent = `You got ${score} out of ${questions.length} (${percent}%).`;
    }

    loadQuestion();
  </script>
</body>
</html>
'''
if __name__ == "__main__":
    app.run(debug=True)


