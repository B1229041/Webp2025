import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'title', headerName: '名稱', flex: 1 },
  { field: 'location', headerName: '地點', flex: 1 },
  { field: 'price', headerName: '票價', flex: 1 }
];

const { useState, useEffect } = React;

function Table() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    fetch(`https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=6`, { method: 'GET' })
      .then(res => res.json())
      .then(response => {
        const datas = response.map(data => ({
          UID: data["UID"],
          title: data["title"],
          location: data["showInfo"][0]?.location || "無資料",
          price: data["showInfo"][0]?.price || "免費"
        }));
        setRows(datas);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div style={{ height: 600, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        getRowId={(row) => row.UID}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 10,
            },
          },
        }}
        pageSizeOptions={[10]}
        sx={{
          '& .MuiDataGrid-columnHeaders': {
            backgroundColor: '#04AA6D',
            color: 'white',
            fontWeight: 'bold',
          },
          '& .MuiDataGrid-cell': {
            border: '1px solid #ddd',
            padding: '6px',
          },
          '& .MuiDataGrid-row:nth-of-type(even)': {
            backgroundColor: '#f2f2f2',
          },
          '& .MuiDataGrid-row:hover': {
            backgroundColor: '#ddd',
          },
          fontFamily: 'Arial, Helvetica, sans-serif',
        }}
      />
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Table />
  </React.StrictMode>
);

reportWebVitals();
