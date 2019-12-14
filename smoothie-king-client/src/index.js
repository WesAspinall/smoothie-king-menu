import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import menu from './menu';

const App = () => {
    console.log(menu)
    return (
        <div className="app">
            {
                menu.map(item => {
                    return (<div className="menu-item" key={Math.random() * 100}>
                   
                        <span className="item-category">{item.category}</span><span>{item.title}</span>
                    </div>)
                })
            }
        </div>
    )
}

ReactDOM.render(<App/>, document.querySelector('#root'));