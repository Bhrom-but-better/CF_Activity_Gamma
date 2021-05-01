import React from 'react'

const Glorified_username = (props) => {
  const {username, rating} = props;
  console.log(username, rating)
  let color = "";
  if(rating >= 3000) color = "black-red";
  else if(rating >= 2400) color = "red";
  else if(rating >= 2100) color = "orange";
  else if(rating >= 1900) color = "violet";
  else if(rating >= 1600) color = "blue";
  else if(rating >= 1400) color = "cyan";
  else if(rating >= 1200) color = "green";
  else color = "grey";
  return (
    <div className={`text-${color} font-bold`}>
      {username}
    </div>
  )
} 

export default Glorified_username;