import './App.css'



function App() {

  return (
    <div className="container">
      <div>
      <h1 className='hel1'>BUG BRAWLERS</h1>
      </div>
      <div className='hel3'>
        <form action="">
          <input type="text" placeholder='Enter .csv file' />
          <button type='submit' id="btn">Enter</button>
        </form>
      </div>
      <div className='hel2'>
        <ul>
          <li>
          <a href="https://bobbyhadz.com" target="_blank" rel="noopener noreferrer">
        <button>Number of results</button>
      </a>
          </li>
          <li>
          <a href="https://bobbyhadz.com" target="_blank" rel="noopener noreferrer">
        <button>Mean Salary</button>
      </a>
          </li><li>
          <a href="https://bobbyhadz.com" target="_blank" rel="noopener noreferrer">
        <button>Median Salary</button>
      </a>
          </li><li>
          <a href="https://bobbyhadz.com" target="_blank" rel="noopener noreferrer">
        <button>25%ile Salary</button>
      </a>
          </li><li>
          <a href="https://bobbyhadz.com" target="_blank" rel="noopener noreferrer">
        <button>75%ile Salary</button>
      </a>
          </li>
        </ul>
      </div>
    </div>
  )
}

export default App
