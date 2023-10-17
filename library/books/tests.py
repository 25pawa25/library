import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from .models import Books, Author


@pytest.mark.django_db
def test_list_books():
    client = APIClient()
    url = reverse('api/books/')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_book():
    client = APIClient()
    url = reverse('api/books/')
    data = {'title': 'Test Book', 'author': 'Test Author'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_retrieve_book():
    book = Books.objects.create(title='Test Book', author='Test Author')
    client = APIClient()
    url = reverse('api/books/<int:pk>', args=[book.id])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_book():
    book = Books.objects.create(title='Test Book', author='Test Author')
    client = APIClient()
    url = reverse('api/books/<int:pk>', args=[book.id])
    data = {'title': 'Updated Book', 'author': 'Updated Author'}
    response = client.put(url, data, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_book():
    book = Books.objects.create(title='Test Book', author='Test Author')
    client = APIClient()
    url = reverse('api/books/<int:pk>', args=[book.id])
    response = client.delete(url)
    assert response.status_code == 204

@pytest.mark.django_db
def test_list_authors():
    client = APIClient()
    url = reverse('api/author/')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_author():
    client = APIClient()
    url = reverse('api/author/')
    data = {'title': 'Test Author', 'phone': '89678765643'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_retrieve_author():
    author = Author.objects.create(title='Test Author', phone='89678765643')
    client = APIClient()
    url = reverse('api/author/<uuid:pk>', args=[author.uuid])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_author():
    author = Author.objects.create(title='Test Author', phone='89678765643')
    client = APIClient()
    url = reverse('api/author/<uuid:pk>', args=[author.uuid])
    data = {'title': 'Updated Book', 'author': 'Updated Author'}
    response = client.put(url, data, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_author():
    author = Author.objects.create(title='Test Author', phone='89678765643')
    client = APIClient()
    url = reverse('api/author/<uuid:pk>', args=[author.uuid])
    response = client.delete(url)
    assert response.status_code == 204



