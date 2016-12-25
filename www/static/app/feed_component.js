import React from "react";
import ReactCSSTransitionGroup from "react-addons-css-transition-group";

class Title extends React.Component {
  render() {
    var style = {
      fontFamily: "Lantinghei SC, Microsoft YaHei, sans-serif",
      fontSize: "1.6em",
      fontWeight: "normal",
      textAlign: "center"
    };

    return (
      <div>
        <p style={style}>{this.props.title}</p>
      </div>
    )
  }
}

class Hr extends React.Component {
  render() {
    var style = {
      border: "none",
      height: 1,
      color: "#EEE",
      backgroundColor: "#EEE",
      marginBottom: "1em",
      clear: "both"
    };

    return (
      <hr style={style} />
    )
  }
}

class ErrMsg extends React.Component {
  constructor(props) {
    super(props);
    this.fadeIn = this.fadeIn.bind(this);
    this.fadeOut = this.fadeOut.bind(this);
    this.state = {show: false, msg: ""};
  }

  fadeIn(msg) {
    this.setState({show: true, message: msg});
  }

  fadeOut() {
    this.setState({show: false});
  }

  render() {
    var style = {
      textAlign: "center",
      fontSize: "0.5em",
      marginBottom: "1em",
      color: "#aaa"
    };

    if (this.state.show) {
      var items = [<span>{this.state.message}</span>,];
    }
    else {
      var items = [];
    }

    return (
      <div style={style}>
        <ReactCSSTransitionGroup component="span" transitionName="err">
          {items}
        </ReactCSSTransitionGroup>
      </div>
    )
  }
}

class Input extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    var v = e.target.value;
    this.props.updateField(this.props.field, v);
  }

  render() {
    var style = {
      backgroundColor: "transparent",
      border: "0.1rem solid #d1d1d1",
      borderRadius: "1px",
      boxShadow: "none",
      boxSizing: "border-box",
      height: "3.2em",
      width: "42em",
      margin: "0em 0em 1.2em 0em",
      display: "block"
    };

    return (
      <input style={style} value={this.props.value} onChange={this.handleChange} type={this.props.type}/>
    )
  }
}

class Label extends React.Component {
  render() {
    var style = {
       fontFamily: "Lantinghei SC, Microsoft YaHei, sans-serif",
      fontSize: "1.0em",
      fontWeight: "normal",
      marginBottom: "0.5em",
      display: "block"
    };

    return (
      <label style={style}>{this.props.desc}</label>
    )
  }
}

class EditBox extends React.Component {
  render() {
    return (
      <div>
        <Label desc={this.props.desc} />
        <Input type={this.props.type} updateField={this.props.updateField} field={this.props.field} value={this.props.value} />
      </div>
    )
  }
}

class Select extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.state = {list: ["null",]};
  }

  componentDidMount() {
    var that = this;

    fetch(this.props.url)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      var err = data["err"];
      if (!err) {
        var list = data["data"];
        that.setState({list: list});
        that.props.updateField(that.props.field, list[0]);
      }
    })
    .catch(function(err) {
      console.log("Error in get category list");
    })
  }

  handleChange(e) {
    var v = e.target.value;
    this.props.updateField(this.props.field, v);
  }

  render() {
    var style = {
      backgroundColor: "transparent",
      border: "0.1rem solid #d1d1d1",
      borderRadius: "1px",
      boxShadow: "none",
      boxSizing: "border-box",
      height: "3.2em",
      width: "42em",
      margin: "0em 0em 1.2em 0em",
      display: "block"
    };
    var list = this.state.list;

    return (
      <select style={style} value={this.props.value} onChange={this.handleChange}>
        {list.map(function(v, index) { return <option key={index} value={v}>{v}</option>; })}
      </select>
    )
  }
}

class SelectBox extends React.Component {
  render() {
    return (
      <div>
        <Label desc={this.props.desc} />
        <Select updateField={this.props.updateField} url={this.props.url} field={this.props.field} value={this.props.value} />
      </div>
    )
  }
}

class Button extends React.Component {
  render() {
    var style = {
      backgroundColor: "transparent",
      border: "0.1rem solid #d1d1d1",
      borderRadius: "0.4rem",
      boxSizing: "borderBox",
      cursor: "pointer",
      display: "inlineBlock",
      fontSize: "0.4rem",
      fontWeight: "700",
      height: "3.2em",
      letterSpacing: "0.3em",
      textAlign: "center",
      textDecoration: "none",
      textTransform: "uppercase",
      whiteSpace: "nowrap"
    };

    return (
      <input style={style} type="submit" value="提交" />
    )
  }
}

export {SelectBox, EditBox, Button, Title, ErrMsg, Hr};