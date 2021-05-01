import React, { useEffect, useState } from 'react'
import Glorified_username from '../components/colored_userame'
import getUsers from '../api/getUsers'
import { Table } from 'antd'
import LoadingOutlined from '@ant-design/icons'

const Users = (props) => {
  const [loading, update_loading] = useState(true);
  const [users, update_users] = useState([]);
  useEffect( () => {
    getUsers(props.organization_id).then( data => {
      update_users(data.map( (d,i) => ({...d, "index": i}) ));
      update_loading(false);
    });
  }, [])

  const columns = [
    {title: "", dataIndex: "index", key: "index", width: "1em" },
    {title: "name", dataIndex: "name", key: "name",
      render: (name, user) => <Glorified_username username={name} rating={user.rating} /> 
    },
    {title: "rating", dataIndex: "rating", key: "rating", sorter: (a, b) => a.rating - b.rating},
  ]

  return (
    <div className="">
      <Table
        bordered={true}
        columns={columns}
        dataSource={users}
        loading={loading}
      />
    </div>
  )
}

export default Users;