import { API_BASE_URL } from "../constants"

const getUsers = async (id) => {
  let data = [];
  try {
    const url = `${API_BASE_URL}/rankings/${id}`;
    const response = await fetch(url);
    console.log(url)
    data = await response.json();
    // data = JSON.parse(data);
    // console.log(data);
    window.x = data;
  }catch(e) {
    console.log(e);
  }
  return data;
}

export default getUsers;