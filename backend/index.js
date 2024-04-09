const express  = require('express')
const app = express()
const mongoose = require('mongoose')
const dotenv = require('dotenv')
dotenv.config()
const cors = require('cors')
const bodyParser = require('body-parser')
const { connect } = require('./connect')
bodyParser.urlencoded({ extended: true })
connect()





app.listen(3000, () => console.log('Server is running on port 3000'))