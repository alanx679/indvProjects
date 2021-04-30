import React, {Component} from 'react';
import { CtxConsumer} from '../index';

class Footer extends Component{

    state = { //component object that holds values
        name: '',
        age: 22,
        isLogin: true
    }

    componentDidMount(){
        this.setState({name: 'MyName'});
    } 

    changed = evt => {
        this.setState({name: evt.target.value});
        console.log(this.state.name);
        //console.log(this.state.name)
    }

    render() {

        //const animals = ['cat', 'dog', 'horse'];
        return (
            <CtxConsumer> 
                {(context) => (
                    <div>
                        {context.animals.map(animal => {
                            return (
                                <div key = {animal}>  
                                    <h1> {animal}</h1> 
                                </div>
                            );    
                        })  } 
                    </div>
                )}
            </CtxConsumer>
        )
    }
    
}
export default Footer;
