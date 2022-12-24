import Word from "../model/words.js";

// Get all words
const getWords = async (req, res) => {
  try {
    const words = await Word.find({}).sort({ createdAt: -1 });
    // const list = words.map((item) => ({
    //   word: item.word,
    //   definition: item.definition,
    // }));
    res.status(200).json({ words });
  } catch (error) {
    res.status(401).json({ msg: error.message });
  }
};

// Get one word
const getWord = async (req, res) => {
  try {
    const word = await Word.findById(req.params.id);
    res.status(200).json(word);
  } catch (error) {
    res.status(401).json({ msg: error.message });
  }
};

// Create word
const createWord = async (req, res) => {
  try {
    const newWord = await Word.create(req.body);
    res.status(200).json(newWord);
  } catch (error) {
    res.status(401).json({ msg: error.message });
  }
};

// Update word
// Update word
const updateWord = async (req, res) => {
  try {
    const word = await Word.findByIdAndUpdate(req.params.id, req.body, {
      runValidators: true,
      new: true,
    });
    res.status(200).json(word);
  } catch (error) {
    res.status(401).json({ msg: error.message });
  }
};

// Delete word
const deleteWord = async (req, res) => {
  try {
    const word = await Word.findByIdAndRemove(req.params.id);
    res.status(200).json({ msg: "deleted succesfully" });
  } catch (error) {
    res.status(401).json({ msg: error.message });
  }
};

export { getWord, getWords, createWord, updateWord, deleteWord };
