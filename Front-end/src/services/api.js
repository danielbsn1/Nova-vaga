export const fetchExample = async () => {
    const response = await fetch ('https://localhost?8000/sua-rota');
    return response.json();

}